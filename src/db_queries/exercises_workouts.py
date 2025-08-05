from db_config import connect_db

# CRUD for exercises_workouts

def get_exercises_by_workout(wid):
    cur, conn = connect_db()
    try:
        # Get exercise IDs linked to the workout
        cur.execute('SELECT eid FROM workout_exercises WHERE wid = %s', (wid,))
        rows = cur.fetchall()
        eids = [row.get('eid') for row in rows]
        
        exercises = []
        for eid in eids:
            cur.execute('SELECT * FROM exercises WHERE id = %s', (eid,))
            exercise_row = cur.fetchone()
            if exercise_row:
                exercises.append(exercise_row)
        
        return exercises

    except Exception as e:
        return f"Error while fetching exercises by workout: {e}"

    finally:
        cur.close()
        conn.close()

    
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
    
