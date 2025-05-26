import unittest
from singer import *
class TestSinger(unittest.TestCase):
    def test_init(self):
        enekes1 = Singer("név1","rock",[("Budapest","07.02"),("Budapest","07.06")])
        self.assertEqual(enekes1._nev, "név1")
        self.assertEqual(enekes1._mufaj, "rock")
        self.assertEqual(len(enekes1._helyszindatum), 2)
    def test_str(self):
        enekes1 = Singer("név1","rock",[("Budapest","07.02"),("Budapest","07.06")])
        expected = "név1,rock:Budapest,07.02;Budapest,07.06;Budapest,06.18"
        self.assertEqual(str(enekes1),expected)
    def test_add(self):
        enekes1 = Singer("név1","rock",[("Budapest","07.02"),("Budapest","07.06")])
        ujkoncert = ("Zamárdi","06.18")
        enekes1_add = enekes1 + ujkoncert
        expected = [("Budapest","07.02"),("Budapest","07.06"),("Zamárdi","06.18")]
        self.assertEqual(enekes1_add._helyszindatum, expected)
    def test_sub(self):
        enekes1 = Singer("név1","rock",[("Budapest","07.02"),("Budapest","07.06")])
        koncert = ("Budapest","07.06")
        enekes1_sub = enekes1 - koncert
        expected = [("Budapest","07.02")]
        self.assertEqual(enekes1_sub._helyszindatum, expected)
    def test_lt_gt(self):
        enekes1 = Singer("név1","rock",[("Budapest","07.02"),("Budapest","07.06")])
        enekes2 = Singer("név2","alternatív",[("Zamárdi","06.10"),("Budapest","06.18"),("Sukoró","07.10")])
        self.assertTrue(enekes1 < enekes2)
        self.assertFalse(enekes1 > enekes2)

class TestConcertOrganizer(unittest.TestCase):
    def test_init(self):
        enekes1 = Singer("név1", "rock", [("Budapest", "07.02")])
        enekes2 = Singer("név2", "pop", [("Zamárdi", "06.10")])
        kontener = ConcertOrganizer([enekes1, enekes2])
        expected = [enekes1, enekes2]
        self.assertEqual(kontener.enekesek, expected)
    def test_str(self):
        enekes1 = Singer("név1", "rock", [("Budapest", "07.02")])
        enekes2 = Singer("név2", "pop", [("Zamárdi", "06.10")])
        kontener = ConcertOrganizer([enekes1, enekes2])
        expected = str(enekes1) + "\n" + str(enekes2)
        self.assertEqual(str(kontener), expected)
    def test_add_singer(self):
        enekes1 = Singer("név1", "rock", [("Budapest", "07.02")])
        enekes2 = Singer("név2", "pop", [("Zamárdi", "06.10")])
        kontener = ConcertOrganizer([enekes1])
        kontener.add_singer(enekes2)
        self.assertIn(enekes2, kontener.enekesek)
        kontener.add_singer(enekes2) #megpróbáljuk újra hozzáadni
        self.assertEqual(len(kontener.enekesek), 2)
    def test_legtobbkoncert(self):
        enekes1 = Singer("név1","rock",[("Budapest","07.02"),("Budapest","07.06")])
        enekes2 = Singer("név2","alternatív",[("Zamárdi","06.10"),("Budapest","06.18"),("Sukoró","07.10")])
        kontener = ConcertOrganizer([enekes1, enekes2])
        self.assertEqual(kontener.legtobbkoncert(), "név2")