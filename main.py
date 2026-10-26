from db import get_connection


def main():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT current_user, current_database();")
            print(cur.fetchone())
    finally:
        conn.close()


if __name__ == "__main__":
    main()
