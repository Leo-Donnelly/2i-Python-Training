import unittest
from TheGreatMorningScramble import choose_room

class TestGreatMorningScramble(unittest.TestCase):

    def test_search_livingroom(self):
        result, found = choose_room.roomChoice("living room")
        self.assertTrue(found)
        self.assertIn("You win, You have found the key.. Now get to work!", result)

    def test_search_bedroom(self):
        result, found = choose_room.roomChoice("bedroom")
        self.assertEqual(found, False)
        self.assertIn("No key here, search elsewhere!", result)

    def test_search_garage(self):
        result, found = choose_room.roomChoice("garage")
        self.assertEqual(found, False)
        self.assertIn("No key here, search elsewhere!", result)

if __name__ == "__main__":
    unittest.main()