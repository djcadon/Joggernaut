from db_config import connect_db

# Adds a new exercise to the exercises table
def new_exercise(uid, name, description):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    INSERT INTO exercises
                    (uid, name, description)
                    VALUES (%s, %s, %s)
                    ''', (uid, name, description))
        conn.commit()

    except Exception as e:
        return f"Error while creating exercise: {e}"

    cur.close()
    conn.close()
    return "Success"

# Updates an existing exercise's name and description by ID
def edit_exercise(id, name, description):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    UPDATE exercises
                    SET name = %s, description = %s
                    WHERE id = %s
                    ''', (name, description, id))
        conn.commit()

    except Exception as e:
        return f"Error while updating exercise: {e}"

    cur.close()
    conn.close()
    return "Success"

# Deletes an exercise by its ID
def delete_exercise(id):
    cur, conn = connect_db()

    try:
        cur.execute('DELETE FROM exercises WHERE id = %s', (id,))
        conn.commit()

    except Exception as e:
        return f"Error while deleting exercise: {e}"

    cur.close()
    conn.close()
    return "Success"

# Fetches a specific exercise by ID
def get_exercise(id):
    cur, conn = connect_db()

    try:
        cur.execute('SELECT * FROM exercises WHERE id = %s', (id,))
        rows = cur.fetchall()

        cur.close()
        conn.close()
        return rows

    except Exception as e:
        cur.close()
        conn.close()
        return f"Error while finding exercise: {e}"

# Gets all exercises created by a specific user
def get_exercise_by_user(uid):
    cur, conn = connect_db()

    try:
        cur.execute('SELECT *  FROM exercises WHERE uid = %s', (uid,))
        rows = cur.fetchall()

        cur.close()
        conn.close()
        return rows

    except Exception as e:
        return f"Error while finding exercises by user: {e}"

# Returns all exercises in the database
def get_all_exercises():
    cur, conn = connect_db()

    try:
        cur.execute('SELECT * FROM exercises')
        rows = cur.fetchall()

        cur.close()
        conn.close()
        return rows

    except Exception as e:
        cur.close()
        conn.close()
        return f"Error while fetching all exercises: {e}"
