from db_config import connect_db

# Create a new workout entry
def new_workout(uid, name, days_of_week):
    cur, conn = connect_db()
    try:
        # Insert new workout into the table
        cur.execute('''
            INSERT INTO workouts (uid, name, days_of_week)
            VALUES (%s, %s, %s)
            RETURNING id, uid, name, days_of_week
        ''', (uid, name, days_of_week))

        workout = cur.fetchone()  # Get the inserted workout info
        conn.commit()  # Save the changes

        return workout

    except Exception as e:
        return f"Error while creating workout: {e}"

    finally:
        # Always close connection after operation
        cur.close()
        conn.close()


# Update an existing workout's name or days
def edit_workout(id, name, days_of_week):
    cur, conn = connect_db()

    try:
        # Update the workout where id matches
        cur.execute('''
                    UPDATE workouts
                    SET name = %s, description = %s
                    WHERE id = %s
                    ''', (name, days_of_week, id))  # Note: description may be incorrect here

        conn.commit()

    except Exception as e:
        return f"Error while updating exercise: {e}"

    cur.close()
    conn.close()

    return "Success"

# Delete a workout by its ID
def delete_workout(id):
    cur, conn = connect_db()

    try:
        cur.execute('DELETE FROM workouts WHERE id = %s', (id, ))
        conn.commit()

    except Exception as e:
        return f"Error while deleting workout: {e}"

    cur.close()
    conn.close()

    return "Success"

# Get a single workout by ID
def get_workout(id):
    cur, conn = connect_db()

    try:
        cur.execute('SELECT * FROM workouts WHERE id = %s', (id, ))
        rows = cur.fetchall()  # Get the result rows

        cur.close()
        conn.close()
        return rows

    except Exception as e:
        cur.close()
        conn.close()
        return f"Error while finding workout: {e}"

# Get all workouts created by a specific user
def get_workouts_by_user(uid):
    cur, conn = connect_db()

    try:
        cur.execute('SELECT * FROM workouts WHERE uid = %s', (uid,))
        rows = cur.fetchall()

        cur.close()
        conn.close()
        return rows

    except Exception as e:
        return f"Error while finding workouts by user: {e}"
