import unittest
from TheGreatMorningScramble import choose_room 

class TestGreatMorningScramble(unittest.TestCase):
    def test_search_livingroom(self):
          result, found = choose_room.roomChoice("living room")
          self.assertTrue(found)
          self.assertIn("You win", result)

    def test_search_bedroom(self):
        result, found = choose_room.roomChoice("bedroom")
        self.assertEqual(found, False)
        self.assertTrue("None" in result)

    def test_search_garage(self):
        result, found = choose_room.roomChoice("garage")
        self.assertEqual(found, False)
        self.assertTrue("None" in result)