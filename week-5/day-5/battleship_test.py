import unittest
from battleship import Arena

class TestArena(unittest.TestCase):
    def get_arena(self):
        arena = Arena([[1,1,0,1,0,0,1,1,1,1],
                       [0,0,0,1,0,0,0,0,0,0],
                       [1,0,0,1,0,1,1,1,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,0],
                       [1,0,0,0,0,1,0,0,0,1],
                       [0,0,0,0,0,1,0,0,0,1],
                       [1,1,0,0,0,0,0,0,0,1],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,1,1,1,1,1,1]])
        return arena

    def test_exists(self):
        self.get_arena()

    def test_is_hit(self):
        self.get_arena()
        self.assertEqual(self.get_arena().is_hit(0,0), True)

    def test_swap(self):
        self.get_arena()
        self.assertEqual(self.get_arena().is_hit(0,0), True)
        self.assertEqual(self.get_arena().swap(0,0), 5)





unittest.main()
