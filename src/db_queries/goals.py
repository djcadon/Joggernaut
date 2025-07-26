from db_config import connect_db

def user_goals(uid):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    SELECT goal_weight FROM goals
                    WHERE uid = %s
                    ''', (uid,))

        rows = cur.fetchall()

        goal_weight = rows[0].get('goal_weight')

        return goal_weight

    except Exception as e:
        return f"Error while retrieving goal weight: {e}"