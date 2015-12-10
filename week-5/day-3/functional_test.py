import unittest
import functional

class TestFunc(unittest.TestCase):

    def setUp(self):
        self._c1 = functional.Character(10,5)
        self._c2 = functional.Character(50,30)

        self._eventlist = [
            {'character': self._c1, 'type': 'damage', 'size': 50},
            {'character': self._c2, 'type': 'damage', 'size': 50},
            {'character': self._c2, 'type': 'heal', 'size': 50}
        ]

    def test_should_handle_the_damage_events(self):
        functional.handle_events(self._eventlist)
        self.assertFalse(self._c1.is_alive())
        self.assertTrue(self._c2.is_alive())

    def test_should_heal_character(self):
        functional.handle_events(self._eventlist)
        self.assertEqual(self._c2.get_health(),100)


    def test_apply_function(self):
        array = [1,2,3]
        self.assertEqual(functional.adder(array),[2,3,4])

    def test_filter_array(self):
        array = [0,1,2,3,4,5,6,7,8,9]
        self.assertEqual(functional.filter_array(array), [0,3,6,9])

unittest.main()
