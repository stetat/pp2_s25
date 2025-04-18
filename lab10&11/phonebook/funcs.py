import psycopg2
from config import load_config

def pagination(limit, offset):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM phonebook
                ORDER BY id
                LIMIT %s OFFSET %s
            """, (limit, offset))
            rows = cur.fetchall()
            for row in rows:
                print(row)


def phone_ptrn(pattern):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""

                SELECT * FROM phonebook
                WHERE phone_number LIKE %s
                                
                """, (f"%{pattern}%",))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print("Error: ", e)

def name_ptrn(pattern):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""

                SELECT * FROM phonebook
                WHERE name LIKE %s
                                
                """, (f"%{pattern}%",))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print("Error: ", e)


t = input("What pattern type do you want? ")

if t == "name":
    pattern = input("Input the pattern: ")
    name_ptrn(pattern)

elif t == "number":
    pattern = input("Input the pattern: ")
    phone_ptrn(pattern)

elif t == "pagin":
    limit = int(input("input limit: "))
    offset = int(input("input offset: "))
    pagination(limit, offset)