
class HighscoreRepository:
    """Class to use SQLite database for handling highscore information
    """

    def __init__(self, DB):
        """Class constructor, takes database connection as parameter.

        Args:
            db (Object): Database connection object.
        """

        self._DB = DB

    def highscores_list(self):
        """Method which returns the highscores database best 3 times per level as 
        a list.

        Returns:
            rows (list): List of tuples (int, float) level number and time.
        """

        cursor = self._DB.cursor()
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
        """Inserts time attack mode times into database with level number.

        Args:
            level (int): Level number to distinquish level.
            time (float): Time indicated with two decimals.
        """
        cursor = self._DB.cursor()
        cursor.execute(
            "insert into highscores (level, time) values (?, ?)",
            (level , time)
        )
        self._DB.commit()