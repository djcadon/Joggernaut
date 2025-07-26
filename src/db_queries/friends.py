from db_config import connect_db
from db_queries.user_metrics import get_user_metrics

def get_all_friends(uid):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    SELECT fid FROM friends
                    WHERE uid = %s
                    ''', (uid,))

        rows = cur.fetchall()

        friend_ids = [i.get('fid') for i in rows]

        friend_details = []
        for id in friend_ids:
            cur.execute('''
                        SELECT name FROM users
                        WHERE id = %s
                        ''', (id))

            name = cur.fetchall()[0].get('name')
            metrics = get_user_metrics(id)

            details = {
                'name': name,
                'weight': metrics.get('weight'),
                'height': metrics.get('height'),
            }

            friend_details.append(details)

        return friend_details

    except Exception as e:
        return f"Error while fetching friends, {e}"