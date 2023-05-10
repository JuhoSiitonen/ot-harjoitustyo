from database_connection import get_db_connection

def initialize_db():
    """Initializes the database and creates highscore table.
    """

    DB = get_db_connection()
    drop_tables(DB)
    create_hs_table(DB)

def create_hs_table(DB):
    """Method to create highscore table with two rows, level number and 
    completion time.
    """

    cursor = DB.cursor()
    cursor.execute("""
        create table highscores (
            level int,
            time float
        );
    """)
    DB.commit()

def drop_tables(DB):
    """Method to drop existing table if re initialized.
    """

    cursor = DB.cursor()
    cursor.execute("""
        drop table if exists highscores;
    """)

    DB.commit()

if __name__ == "__main__":
    initialize_db()
