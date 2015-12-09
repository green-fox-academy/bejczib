import unittest
from decorator import Mithical, Bow

class TestDecorator(unittest.TestCase):
    def test_mithical_bow(self):
        weapon = Mithical(Bow())
        self.assertEqual(weapon.damage(Bow()), 45)


unittest.main()
