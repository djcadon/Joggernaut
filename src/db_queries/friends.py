from db_config import connect_db
from db_queries.user_metrics import get_user_metrics

def new_friend_connection(uid, fid):
    cur, conn = connect_db()

    try:
        # See if it exists already
        cur.execute('''
                    SELECT * FROM friends
                    WHERE (fid = %s AND uid = %s) OR (fid = %s AND uid = %s)
                    ''', (fid, uid, uid, fid))

        rows = cur.fetchall()

        if len(rows) > 0:
            return "Friendship already exists! Go hug"

        else:
            cur.execute('''
                        INSERT INTO friends
                        (uid, fid)
                        VALUES (%s, %s)
                        ''', (uid, fid))

            conn.commit()

            # Saving the inverse too, to avoid anomalies
            cur.execute('''
                        INSERT INTO friends
                        (uid, fid)
                        VALUES (%s, %s)
                        ''', (fid, uid))

            conn.commit()

        cur.close()
        conn.close()

        return "Success"
    except Exception as e:
        return f"Error while adding friend connection: {e}"

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

def delete_friend_connection(uid, fid):
    cur, conn = connect_db()

    try:
        cur.execute('''
                    DELETE from friends
                    WHERE (uid = %s AND fid = %s) OR (fid = %s AND uid = %s)
                    ''', (uid, fid, fid, uid))

        conn.commit()

        cur.close()
        conn.close()
        return "Success"

    except Exception as e:
        return f"Error while deleting friend connection: {e}"