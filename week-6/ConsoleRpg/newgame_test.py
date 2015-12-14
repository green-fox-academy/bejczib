import unittest
from menu import *


class TestMenu(unittest.TestCase):
    def test_display_name(self):
        new = NewGame()
        self.assertEqual(new.display_name('Balint',), 'Balint' )

    def test_get_menu(self):
        new = NewGame()
        self.assertEqual(new.get_menu(), {'1': 'Reenter Name', '2': 'Continue', '3': 'Quit'})

unittest.main()
