import psycopg2
from config import load_config

def create_tables():
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""

                CREATE TABLE users(               
                id SERIAL PRIMARY KEY,
                player TEXT UNIQUE NOT NULL,
                level INT DEFAULT 1
                );

                CREATE TABLE user_score (
                id SERIAL PRIMARY KEY,
                player_id INT REFERENCES users(id) ON DELETE CASCADE,
                score INT NOT NULL,
                saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                snake_position TEXT,
                direction TEXT,
                food_position TEXT
                );             
                
                """)
    except Exception as e:
        print("Error: ", e)


create_tables()
