import psycopg2
from config import load_config

def update_bname(name, number):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                UPDATE phonebook
                SET phone_number = %s
                WHERE name = %s
            
                
                """, (number, name))
    except Exception as e:
        print("Error: ", e)


def update_bnumber(name, number):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                UPDATE phonebook
                SET name = %s
                WHERE phone_number = %s
            
                
                """, (name, number))
    except Exception as e:
        print("Error: ", e)


t = input("What do you want to change? (name, number): ")
if t == "number":
    nam = input("Input an existing name: ")
    num = input("Input a new number: ")
    update_bname(nam, num)

else:
    nam = input("Input a new name: ")
    num = input("Input an existing number: ")
    update_bnumber(nam, num)


