import psycopg2
from config import load_config

def insert_one(name, phone_number):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO phonebook(name, phone_number)
                    VALUES(%s, %s)

                """, (name, phone_number))
    except Exception as e:
        print("Error:", e)


n = input("Enter the name: ")
p = input("Enter the phone number: ")

try:
    insert_one(n, p)
    print("Inserted into phonebook successfully")
except Exception as e:
    print("Erorr: ", e)
    

