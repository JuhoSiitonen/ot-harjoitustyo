import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "data", DATABASE_FILENAME)

LEVELS_FILENAME = os.getenv("LEVELS_FILENAME") or "levels.txt"
LEVELS_FILE_PATH = os.path.join(dirname, "data", LEVELS_FILENAME)

CELL_SIZE = 64
DISPLAY_WIDTH = 1200
