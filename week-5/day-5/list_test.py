import unittest
from list import MyMagic

class ListTest(unittest.TestCase):

    def setUp(self):
        self.names = [{ 'id': 1, 'name': 'John'},
                      { 'id': 2, 'name': 'Molly'},
                      { 'id': 3, 'name': 'Jane'}]

    def test_array_of_names(self):
        my_list = MyMagic(self.names)
        self.assertEqual(my_list.array_of_names(), ['John', 'Molly', 'Jane'])

    def test_name_starts_with_j(self):
        my_list = MyMagic(self.names)
        self.assertEqual(my_list.names_with_j(), ['John', 'Jane'])

unittest.main()
