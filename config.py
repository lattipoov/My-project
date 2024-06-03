from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv('TOKEN')
DB_ADDRESS = getenv('DB_ADDRESS')
DB_PORT = getenv('DB_PORT')
DB_USER = getenv('DB_USER')
DB_PASS = getenv('DB_PASS')
DB_NAME = getenv('DB_NAME')