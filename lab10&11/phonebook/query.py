import psycopg2
from config import load_config

def get_data(query):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    
    except Exception as e:
        print("Error: ", e)

query = input("Input a SQL query: ")
get_data(query)