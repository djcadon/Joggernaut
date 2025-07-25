from src.db_config import connect_db

def new_metric(height, weight, uid):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    INSERT INTO user_metrics
                    (uid, height, weight)
                    VALUES (%s, %s, %s)
                    ''', (uid, height, weight))
        
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        return f"Error while entering new metric: {e}"

    return "Success, User metric created successfully" 