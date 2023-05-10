from database_connection import get_db_connection

class HighscoreRepository:
    def __init__(self, db):
        self._db = db

    def highscores_list(self):
        cursor = self._db.cursor()
        cursor.execute("""
            select level, time 
            from (
                select level, time , ROW_NUMBER() 
                over (partition by level order by time)
                as row_num
                from highscores
            ) as ranked
            where row_num <= 3;
        """)
        rows = cursor.fetchall()
        return rows
    
    def insert_into_highscores(self, level, time):
        cursor = self._db.cursor()
        cursor.execute(
            "insert into highscores (level, time) values (?, ?)",
            (level , time)
        )
        self._db.commit()
