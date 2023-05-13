import unittest
from repositories.highscore_repository import HighscoreRepository
from database_connection import get_db_connection


class TestHighscoreRepository(unittest.TestCase):
    def setUp(self):
        database = get_db_connection()
        self.highscore_rep = HighscoreRepository(database)

    def test_db_empty(self):
        temp = self.highscore_rep.highscores_list()
        self.assertEqual(temp, [])

    def test_insertion_works(self):
        self.highscore_rep.insert_into_highscores(1, 1)
        temp = self.highscore_rep.highscores_list()
        self.assertNotEqual(temp, [])

    def test_insertion_and_deletion_works(self):
        self.highscore_rep.insert_into_highscores(1, 1)
        self.highscore_rep.erase_highscores()
        temp = self.highscore_rep.highscores_list()
        self.assertEqual(temp, [])