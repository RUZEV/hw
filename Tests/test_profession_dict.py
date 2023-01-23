import unittest
import Prof_List as PR

class json_search_test(unittest.TestCase):
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=json_search(key1, items))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, items))

    def test_is_a_dict(self):
        '''Shold return a dict'''
        self.assertIsInstance(fetch(key1, items), dict)