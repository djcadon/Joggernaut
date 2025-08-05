from db_config import connect_db

# CRUD for exercises_workouts

def get_exercises_by_workout(wid):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    SELECT e.* FROM exercises e
                    JOIN workout_exercises we ON e.id = we.eid
                    WHERE we.wid = %s
                    ''', (wid,))

        rows = cur.fetchall()

        cur.close()
        conn.close()
        return rows

    except Exception as e:
        cur.close()
        conn.close()
        return f"Error while finding exercises by workout: {e}"
    
def add_exercise_to_workout(wid, eid):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    INSERT INTO workout_exercises (wid, eid)
                    VALUES (%s, %s)
                    ''', (wid, eid))

        conn.commit()

        cur.close()
        conn.close()
        return "Success"
    except Exception as e:
        return f"Error while adding exercise to workout: {e}"
    
def remove_exercise_from_workout(wid, eid):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    DELETE FROM workout_exercises
                    WHERE wid = %s AND eid = %s
                    ''', (wid, eid))

        conn.commit()

        cur.close()
        conn.close()
        return "Success"
    except Exception as e:
        return f"Error while removing exercise from workout: {e}"
    
def update_exercise_in_workout(wid, old_eid, new_eid):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    UPDATE workout_exercises
                    SET eid = %s
                    WHERE wid = %s AND eid = %s
                    ''', (new_eid, wid, old_eid))

        conn.commit()

        cur.close()
        conn.close()
        return "Success"
    except Exception as e:
        return f"Error while updating exercise in workout: {e}"
    
