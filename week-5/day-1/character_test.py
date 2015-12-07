import unittest
from character import Character

class TestCharacter(unittest.TestCase):
    def test_exists(self):
        character = Character('Test', 100, 10)

    def test_properties(self):
        character = Character('Test', 100, 10)
        self.assertEqual(character.name, 'Test')
        self.assertEqual(character.hp, 100)
        self.assertEqual(character.damage, 10)

    def test_drink_potion(self):
        character = Character('Test', 100, 10)
        character.drink_potion()
        self.assertEqual(character.hp, 110)

    def test_strike(self):
        character = Character('Test', 100, 10)
        opponent = Character('Opponent', 100, 10)
        character.strike(opponent)
        self.assertEqual(opponent.hp, 90)

    def test_status(self):
        character = Character('Test', 100, 10)


unittest.main()
