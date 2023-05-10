import sqlite3
from settings import DATABASE_FILE_PATH

db = sqlite3.connect(DATABASE_FILE_PATH)
db.row_factory = sqlite3.Row


def get_db_connection():
    """Method to create database connection object to use by other modules.

    Returns:
        db (object): Database connection object.
    """

    return db
