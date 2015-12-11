import unittest
from duplicate_encoder import *

class TestDuplicateEncoder(unittest.TestCase):
    def test_exists(self):
        string = MyString('')
        self.assertEqual(string.duplicate_encoder(), '')

    def test_different_letter(self):
        string = MyString('din')
        self.assertEqual(string.duplicate_encoder(), '(((')

    def test_same_letter(self):
        string = MyString('aaa')
        self.assertEqual(string.duplicate_encoder(), ')))')

    def test_complicated_letter(self):
        string = MyString('success')
        self.assertEqual(string.duplicate_encoder(), ')())())')

    def test_ignore_capitalization(self):
        string = MyString('Success')
        self.assertEqual(string.duplicate_encoder(), ')())())')

    def test_fucking_codewars(self):
        string = MyString('(( @')
        self.assertEqual(string.duplicate_encoder(), '))((')


unittest.main()
