import unittest
from character import *

class TestCharacter(uittest.TestCase):
    ch = Character('Balint', 0, 0, 0)
    def test_roll_luck(self):
        self.assertEqual(ch.luck,  )
