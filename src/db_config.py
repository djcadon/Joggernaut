# Import database config values and psycopg2 for PostgreSQL connection
from config import DB_PORT, DB_NAME, DB_HOST, DB_PASSWORD, DB_USER
import psycopg2
from psycopg2.extras import RealDictCursor

# Try block to handle connection issues
try:
    # Function to connect to the PostgreSQL database
    def connect_db():
        conn = psycopg2.connect(
            host=DB_HOST,              # Hostname (e.g., localhost)
            port=DB_PORT,              # Port number (usually 5432)
            user=DB_USER,              # Database username
            password=DB_PASSWORD,      # Database password
            dbname=DB_NAME,            # Name of the database
            cursor_factory=RealDictCursor  # Makes cursor return rows as dictionaries
        )
        cur = conn.cursor()  # Create a cursor object for executing SQL commands

        return cur, conn     # Return cursor and connection objects
except Exception as e:
    print("Connection Failed: ", e)  # Print the error if connection fails

