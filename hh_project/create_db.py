import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import DB_CONFIG


def create_database():
    """Create database hh_vacancies."""
    try:
        # Connect to PostgreSQL server
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_CONFIG["database"],))
        exists = cursor.fetchone()

        if exists:
            print(f"Database '{DB_CONFIG['database']}' already exists!")
        else:
            cursor.execute(f"CREATE DATABASE {DB_CONFIG['database']};")
            print(f"Database '{DB_CONFIG['database']}' created successfully!")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    create_database()
