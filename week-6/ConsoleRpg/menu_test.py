import unittest
from menu import *


class TestMenu(unittest.TestCase):
    def test_exists(self):
        menu = Menu()

    def test_get_menu_items(self):
        menu = Menu()
        self.assertEqual(menu.get_menu(), {'1': 'New Game', '2': 'Load Game', '3': 'Exit'})

    def test_submenu_existance(self):
        new = NewGame()
        load = LoadGame()
        quit = QuitGame()

    def test_select_menu_item(self):
        new = NewGame()
        self.assertEqual(new.enter_menu('1'), 'Oh Yeah!!')

    def test_input_incorrect(self):
        menu = Menu()
        self.assertEqual(menu.select_menu('g'), 'Incorrect answer!')

unittest.main()
