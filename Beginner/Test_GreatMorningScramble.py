import unittest

from TheGreatMorningScramble import Search_Room

class TestGreatMorningScramble(unittest.TestCase):

    def test_search_room_kitchen(self):
        result, found = Search_Room("Kitchen")
        self.assertIn("No Key Found", result)
        self.assertFalse(found)

    def test_search_room_livingroom(self):
        result, found = Search_Room("Livingroom")
        self.assertIn("No Key Found", result)
        self.assertFalse(found)

    def test_search_room_bathroom(self):
        result, found = Search_Room("Bathroom")
        self.assertIn("No Key Found", result)
        self.assertFalse(found)

    def test_search_room_bedroom(self):
        result, found = Search_Room("Bedroom")
        self.assertIn("No Key Found", result)
        self.assertFalse(found)

    def test_search_room_garage(self):
        result, found = Search_Room("Garage")
        self.assertTrue(found)
        self.assertIn("You found the key! :D", result)
        

if __name__ == '__main__':
    unittest.main()