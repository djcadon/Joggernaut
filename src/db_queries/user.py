from db_config import connect_db
from werkzeug.security import generate_password_hash, check_password_hash
from db_queries.user_metrics import new_metric
from datetime import date

def new_user(username, password, dob, height, weight, goal_weight):
    hashed_pwd = generate_password_hash(password)

    cur, conn = connect_db()

    try:
        cur.execute('''
                    INSERT INTO users
                    (name, password, dob) VALUES (%s, %s, %s)
                    RETURNING id
                    ''', (username, hashed_pwd, dob))
        uid = cur.fetchall()[0].get('id')
        conn.commit()

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

    new_metric(height, weight, uid)

    return ("Success", id)

def login(username, password):
    cur, conn = connect_db()
    try:
        cur.execute('SELECT id, password FROM users WHERE name = %s', (username,))
        rows = cur.fetchall()
        hashed_pwd = rows[0].get('password')
        id = rows[0].get('id')

        cur.close()
        conn.close()

        if check_password_hash(hashed_pwd, password) == True:
            return ("Success", id)

        else:
            return ("Incorrect username or password", 0)

    except Exception as e:
        return f"Error while logging in: {e}"

def find_user_age(username):
    cur, conn = connect_db()

    try:
        cur.execute('SELECT dob FROM users WHERE name = %s', (username,))
        dob = cur.fetchall()[0].get('dob')
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        cur.close()
        conn.close()

        return age

    except Exception as e:
        return f"Error retrieving age: {e}"