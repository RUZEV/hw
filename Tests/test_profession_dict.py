import unittest
import dictionary_for_test as dt

class json_search_test(unittest.TestCase):
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=dt.fetch(dt.key1, dt.items))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == dt.fetch(dt.key2, dt.items))

    def test_is_a_dict(self):
        '''Shold return a dict'''
        self.assertIsInstance(dt.fetch(dt.key1, dt.items), dict)