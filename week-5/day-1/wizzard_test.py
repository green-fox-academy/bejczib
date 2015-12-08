import unittest
from wizzard import Wizzard


class TestWizzard(unittest.TestCase):
    def test_existance(self):
        wizzard = Wizzard('Merlin', 40, 10, 20)

    def test_inheritance(self):
        wizzard = Wizzard('Merlin', 40, 10, 20)
        self.assertEqual(wizzard.hp, 40)

    def test_manna(self):
        wizzard = Wizzard('Merlin', 40, 10, 20)
        self.assertEqual(wizzard.manna, 20)

    def test_strike(self):
        wizzard = Wizzard('Merlin', 40, 10, 20)
        opponent = Wizzard('Voldemort', 50, 12, 30)
        wizzard.strike(opponent)
        self.assertEqual(wizzard.manna, 15)
        self.assertEqual(opponent.hp, 20)

    def test_strike_manna_reduction(self):
        wizzard = Wizzard('Merlin', 40, 10, 20)
        opponent = Wizzard('Voldemort', 50, 12, 30)
        wizzard.strike(opponent)
        self.assertEqual(wizzard.manna, 15)

    def test_manna_strike(self):
        wizzard = Wizzard('Merlin', 40, 10, 4)
        opponent = Wizzard('Voldemort', 50, 12, 30)
        wizzard.strike(opponent)
        self.assertEqual(wizzard.manna, 4)
        self.assertEqual(opponent.hp, 50 - 10/3)

unittest.main()
