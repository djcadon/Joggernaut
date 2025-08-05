from db_config import connect_db

# CRUD for progress entries

def new_progress_entry(uid, eid, wid, weight, duration_mins):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    INSERT INTO progress
                    (uid, eid, wid, weight, duration_mins)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ''', (uid, eid, wid, weight, duration_mins))

        conn.commit()


        cur.close()
        conn.close()
        return "Success"
    

    except Exception as e:
        return f"Error while recording new progress entry: {e}"

def edit_progress_entry(id, eid, wid, weight, duration_mins):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    UPDATE progress
                    SET eid = %s, wid = %s, weight = %s, duration_mins = %s
                    WHERE id = %s
                    ''', (eid, wid, weight,  duration_mins, id))

        conn.commit()

        cur.close()
        conn.close()
        return "Success"

    except Exception as e:
        return f"Error while updating progress record: {e}"

def delete_progress_entry(id):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    DELETE FROM progress
                    WHERE id = %s
                    ''', (id, ))

        conn.commit()

        cur.close()
        conn.close()

        return "Success"
    except Exception as e:
        return f"Error while deleting progress record: {e}"

def get_progress_by_exercise(uid, eid):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    SELECT * FROM progress
                    WHERE uid = %s AND eid = %s
                    ''', (uid, eid))

        progress = cur.fetchall()

        cur.close()
        conn.close()

        return progress

    except Exception as e:
        return f"Error when retrieving progress: {e}"