import psycopg2

class Database:
    def __init__(self):
        self.db_params = {
            'dbname': 'rs',
            'user': 'username',
            'password': 'password',
            'host': 'localhost',
            'port': '5432'
        }

    def connect(self):
        return psycopg2.connect(**self.db_params)

    def login_user(self, username, password):
        user = None
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            if user:
                user = dict(zip([desc[0] for desc in cursor.description], user))
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
        return user

    def get_user(self, id):
        user = None
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            user = cursor.fetchone()
            if user:
                user = dict(zip([desc[0] for desc in cursor.description], user))
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
        return user

    def get_items(self, ids):
        items = []
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id = ANY(%s::int[])", (ids,))
            rows = cursor.fetchall()
            items = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
        return items

    def get_items_with_score(self, ids_cores):
        items = []
        try:
            conn = self.connect()
            cursor = conn.cursor()
            ids = [id_score[0] for id_score in ids_cores]
            cursor.execute("SELECT * FROM products WHERE id = ANY(%s::int[])", (ids,))
            rows = cursor.fetchall()
            items = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
        # add score to items
        for item in items:
            item['score'] = next(id_score[1] for id_score in ids_cores if id_score[0] == item['id'])
        return items

    def get_item_by_id(self, id):
        item = None
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            row = cursor.fetchone()
            if row:
                item = dict(zip([desc[0] for desc in cursor.description], row))
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
        return item

    def get_items_ids(self):
        items_ids = []
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM products")
            rows = cursor.fetchall()
            items_ids = [row[0] for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
        return items_ids

    def get_rand_items(self, k):
        items = []
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products ORDER BY RANDOM() LIMIT %s", (k,))
            rows = cursor.fetchall()
            items = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
        return items
