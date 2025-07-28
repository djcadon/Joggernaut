from db_config import connect_db

# Making CRUD for workouts
def new_workout(uid, name, days_of_week):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    INSERT INTO workouts
                    (uid, name, days_of_week)
                    VALUES (%s, %s, %s)
                    ''', (uid, name, days_of_week))

        conn.commit()

    except Exception as e:
        return f"Error while creating workouts: {e}"

    cur.close()
    conn.close()
    return "Success"


def edit_workout(id, name, days_of_week):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    UPDATE workouts
                    SET name = %s, description = %s
                    WHERE id = %s
                    ''', (name, days_of_week, id))

        conn.commit()

    except Exception as e:
        return f"Error while updating exercise: {e}"

    cur.close()
    conn.close()

    return "Success"

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

def get_workout(id):
    cur, conn = connect_db()

    try:
        cur.execute('SELECT * FROM workouts WHERE id = %s', (id, ))

        rows = cur.fetchall()

        cur.close()
        conn.close()
        return rows

    except Exception as e:
        cur.close()
        conn.close()
        return f"Error while finding workout: {e}"

def get_workouts_by_user(uid):
    cur, conn = connect_db()

    try:
        cur.execute('SELECT *  FROM workouts WHERE uid = %s', (uid,))

        rows = cur.fetchall()

        cur.close()
        conn.close()
        return rows

    except Exception as e:
        return f"Error while finding workouts by user: {e}"