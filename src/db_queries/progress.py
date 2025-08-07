from db_config import connect_db

# CRUD for progress entries

def new_progress_entry(uid, eid, wid, weight, duration_mins):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    INSERT INTO progress
                    (uid, eid, wid, weight, duration_mins)
                    VALUES (%s, %s, %s, %s, %s)
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
                SELECT e.name as ex_name, w.name as w_name, p.weight, p.duration_mins, p.created_at
                FROM exercises e, workouts w, progress p
                WHERE e.id = p.eid AND w.id = p.wid AND p.uid = %s AND e.id = %s
                    ''', (uid, eid))

        progress = cur.fetchall()

        cur.close()
        conn.close()

        return progress

    except Exception as e:
        return f"Error when retrieving progress: {e}"


def get_all_progress_records(uid):
    cur, conn = connect_db()

    query = '''
    SELECT e.name as ex_name, w.name as w_name, p.weight, p.duration_mins
    FROM exercises e, workouts w, progress p
    WHERE e.id = p.eid AND w.id = p.wid AND p.uid = %s
    '''

    try:
        cur.execute(query, (uid,))

        rows = cur.fetchall()

        cur.close()
        conn.close()

    except Exception as e:
        return f"Error while fetching progress records: {e}"

    return rows