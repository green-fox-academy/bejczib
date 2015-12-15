import unittest
from menu import *
from commands import *


class TestMenu(unittest.TestCase):

    items = [
             MenuItems(1, 'New Game', display_name),
            ]

    def test_select_menu(self):
        menu = Menu(self.items)
        self.assertEqual(menu.select_menu(1), 'Balint')

unittest.main()
