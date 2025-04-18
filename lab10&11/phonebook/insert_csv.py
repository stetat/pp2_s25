import psycopg2
import csv
from config import load_config

def insert_csv(filename):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        cur.execute("""
                            INSERT INTO phonebook(name, phone_number)
                            VALUES(%s, %s)

                            """, (row["name"], row["phone_number"]))
    except Exception as e:
        print("Error:", e)



insert_csv("data.csv")
    

