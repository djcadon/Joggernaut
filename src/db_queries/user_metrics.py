from db_config import connect_db

# Create a new entry in the user_metrics table
def new_metric(height, weight, uid):
    cur, conn = connect_db()

    try:
        # Insert the user's height and weight into the database
        cur.execute('''
                    INSERT INTO user_metrics
                    (uid, height, weight)
                    VALUES (%s, %s, %s)
                    ''', (uid, height, weight))
        
        conn.commit()  # Save the changes
        cur.close()
        conn.close()

    except Exception as e:
        return f"Error while entering new metric: {e}"

    return "Success, User metric created successfully"

# Get the user's metrics (height and weight) using their user ID
def get_user_metrics(uid):
    cur, conn = connect_db()

    try:
        # Query the user_metrics table for the given user ID
        cur.execute('''
                    SELECT * FROM user_metrics
                    WHERE uid = %s
                    ''', (uid,))

        rows = cur.fetchall()[0]  # Get the first (and only) row

        return rows

    except Exception as e:
        return f"Error!, {e}"
