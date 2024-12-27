
import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'rs',
    'user': 'username',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

def login_user(username, password):
    user = None
    try:
        conn = psycopg2.connect(**db_params)
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

def get_user(id):
    user = None
    try:
        conn = psycopg2.connect(**db_params)
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

def get_items(ids):
    items = []
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ANY(%s)", (ids,))
        rows = cursor.fetchall()
        items = [dict(zip([desc[0] for desc in cursor.description], row)) for row in rows]
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()
    return items

def get_items_ids():
    items_ids = []
    try:
        conn = psycopg2.connect(**db_params)
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