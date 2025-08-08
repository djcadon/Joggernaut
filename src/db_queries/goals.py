from db_config import connect_db

# Fetches the goal weight for a specific user
def user_goals(uid):
    cur, conn = connect_db()

    try:
        # Get the goal weight for the user
        cur.execute('''
                    SELECT goal_weight FROM goals
                    WHERE uid = %s
                    ''', (uid,))
        rows = cur.fetchall()

        goal_weight = rows[0].get('goal_weight')  # Extract goal weight from first row
        return goal_weight

    except Exception as e:
        return f"Error while retrieving goal weight: {e}"
