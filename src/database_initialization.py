from database_connection import get_db_connection

def initialize_db():

    db = get_db_connection()
    drop_tables(db)
    create_hs_table(db)

def create_hs_table(db):
    cursor = db.cursor()
    cursor.execute("""
        create table highscores (
            level int,
            time float
        );
    """)
    db.commit()

def drop_tables(db):

    cursor = db.cursor()
    cursor.execute("""
        drop table if exists highscores;
    """)

    db.commit()

if __name__ == "__main__":
    initialize_db()
