import sqlite3
from settings import DATABASE_FILE_PATH

db = sqlite3.connect(DATABASE_FILE_PATH)
db.row_factory = sqlite3.Row


def get_db_connection():
    return db