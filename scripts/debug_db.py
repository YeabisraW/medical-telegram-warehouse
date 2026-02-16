import psycopg2

def test_configs():
    # Try different common local setups
    attempts = [
        {"host": "localhost", "user": "postgres", "password": "password", "database": "postgres"},
        {"host": "localhost", "user": "postgres", "password": "admin", "database": "postgres"},
        {"host": "localhost", "user": "postgres", "password": "root", "database": "postgres"},
        {"host": "127.0.0.1", "user": "postgres", "password": "password", "database": "telegram_db"},
    ]
    
    for config in attempts:
        try:
            print(f"Trying: {config['user']}@{config['database']}...")
            conn = psycopg2.connect(**config, connect_timeout=3)
            print(f"✅ SUCCESS! Use these settings: {config}")
            
            # Now let's see what databases actually exist
            cur = conn.cursor()
            cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
            dbs = [r[0] for r in cur.fetchall()]
            print(f"Available Databases on your PC: {dbs}")
            return config, dbs
        except Exception as e:
            print(f"❌ Failed: {e}")

test_configs()