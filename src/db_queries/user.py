from db_config import connect_db
from werkzeug.security import generate_password_hash, check_password_hash
from db_queries.user_metrics import new_metric
from datetime import date

# Create a new user and set their goal and metrics
def new_user(username, password, dob, height, weight, goal_weight):
    hashed_pwd = generate_password_hash(password)  # Hash the password before saving

    cur, conn = connect_db()

    try:
        # Insert user and get the new user's ID
        cur.execute('''
                    INSERT INTO users
                    (name, password, dob) VALUES (%s, %s, %s)
                    RETURNING id
                    ''', (username, hashed_pwd, dob))
        uid = cur.fetchall()[0].get('id')
        conn.commit()

        # Insert the user's goal weight
        cur.execute('''
                    INSERT INTO goals
                    (uid, goal_weight) VALUES
                    (%s, %s)
                    ''', (uid, goal_weight))
        conn.commit()

        cur.close()
        conn.close()

    except Exception as e:
        return f"Error while creating user: {e}"

    # Save user metrics like height and weight
    new_metric(height, weight, uid)

    return ("Success", uid)

# Login: check if username and password match
def login(username, password):
    cur, conn = connect_db()
    try:
        # Get stored password hash
        cur.execute('SELECT id, password FROM users WHERE name = %s', (username,))
        rows = cur.fetchall()
        hashed_pwd = rows[0].get('password')
        id = rows[0].get('id')

        cur.close()
        conn.close()

        # Check if entered password matches the stored hash
        if check_password_hash(hashed_pwd, password) == True:
            return ("Success", id)
        else:
            return ("Incorrect username or password", 0)

    except Exception as e:
        return f"Error while logging in: {e}"

# Calculate user's age using their date of birth
def find_user_age(username):
    cur, conn = connect_db()

    try:
        cur.execute('SELECT dob FROM users WHERE name = %s', (username,))
        dob = cur.fetchall()[0].get('dob')
        today = date.today()

        # Calculate age by comparing DOB and today's date
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        cur.close()
        conn.close()

        return age

    except Exception as e:
        return f"Error retrieving age: {e}"

# Get user details using ID
def get_user(id):
    cur, conn = connect_db()

    try:
        cur.execute('SELECT id, name, dob FROM users WHERE id = %s', (id, ))

        rows = cur.fetchone()

        cur.close()
        conn.close()

        return rows
    except Exception as e:
        return f"Error while retrieving user: {e}"

# Search users with similar names using similarity score
def search_user(username):
    cur, conn = connect_db()
    query = '''
    SELECT id, similarity(name, %s) AS sim
    FROM users
    WHERE similarity(name, %s) > 0.30
    ORDER BY sim DESC;
    '''

    try:
        cur.execute(query, (username, username))

        rows = cur.fetchall()

        cur.close()
        conn.close()

        # Get user info for each similar name found
        user_info = []
        for row in rows:
            user_info.append(get_user(row.get('id')))

        return user_info

    except Exception as e:
        return f"Error while finding similar users: {e}"
