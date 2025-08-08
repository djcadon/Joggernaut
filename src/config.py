# Load environment variables from a .env file
from dotenv import load_dotenv
import os

# Load the contents of the .env file into environment variables
load_dotenv()

# Retrieve database connection values from environment variables
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
