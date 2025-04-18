import psycopg2
from config import load_config

def delete_byname(name):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM phonebook WHERE name = %s
                """, (name, ))
    
    except Exception as e:
        print("Error: ", e)



def delete_bynumber(number):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM phonebook WHERE phone_number = %s
                """, (number, ))
    
    except Exception as e:
        print("Error: ", e)


t = input("What do you want to delete?: ")

if t == "name":
    nam = input("Input an existing name: ")
    delete_byname(nam)
else:
    num = input("input an existing number: ")
    delete_bynumber(num)
