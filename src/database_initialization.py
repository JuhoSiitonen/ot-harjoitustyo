from database_connection import get_db_connection

def initialize_db():
    """Initializes the database and creates highscore table.
    """

    database = get_db_connection()
    drop_tables(database)
    create_hs_table(database)

def create_hs_table(database):
    """Method to create highscore table with two rows, level number and 
    completion time.
    """

    cursor = database.cursor()
    cursor.execute("""
        create table highscores (
            level int,
            time float
        );
    """)
    database.commit()

def drop_tables(database):
    """Method to drop existing table if re initialized.
    """

    cursor = database.cursor()
    cursor.execute("""
        drop table if exists highscores;
    """)

    database.commit()

if __name__ == "__main__":
    initialize_db()
