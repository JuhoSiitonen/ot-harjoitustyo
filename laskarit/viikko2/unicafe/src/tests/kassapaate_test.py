import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate(100000)

    def test_luodun_kassapaatteen_saldo_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_lounaiden_maara_nolla(self):
        self.assertEqual((self.kassapaate.edulliset + self.kassapaate.maukkaat), 0)

    def test_
