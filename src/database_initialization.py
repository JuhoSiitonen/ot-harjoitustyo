from database_connection import get_db_connection

def initialize_db():
    """Initializes the database and creates highscore table.
    """

    db = get_db_connection()
    drop_tables(db)
    create_hs_table(db)

def create_hs_table(db):
    """Method to create highscore table with two rows, level number and 
    completion time.
    """

    cursor = db.cursor()
    cursor.execute("""
        create table highscores (
            level int,
            time float
        );
    """)
    db.commit()

def drop_tables(db):
    """Method to drop existing table if re initialized.
    """

    cursor = db.cursor()
    cursor.execute("""
        drop table if exists highscores;
    """)

    db.commit()

if __name__ == "__main__":
    initialize_db()
