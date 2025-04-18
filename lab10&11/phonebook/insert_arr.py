import psycopg2
from config import load_config
import re

def is_valid_phone(phone):

    return re.match(r'^\+?\d{10,}$', phone)

def insert_multiple_users(names, phones):
    config = load_config()
    invalid_entries = []

    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            for name, phone in zip(names, phones):
                if is_valid_phone(phone):
                    cur.execute(
                        "INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)",
                        (name, phone)
                    )
                else:
                    invalid_entries.append((name, phone))

    return invalid_entries


names = ['Beknur', 'Aza', 'Ilyas']
phones = ['87071234567', 'chotambachotam', '+77081234567']

invalids = insert_multiple_users(names, phones)

print("Invalid entries:", invalids)

