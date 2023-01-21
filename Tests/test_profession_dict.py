import unittest
import Prof_List as PR

class MyClass(object):
    def __init__(self, foo):
        if foo != 1:
            raise ValueError('foo is not equal to 1!')
class MyClass2(object):
    def __init__(self):
        pass
class TestPars(unittest.TestCase):
    def test_format(self):
        self.assertDictEqual(Tests)

class json_search_test(unittest.TestCase):
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=json_search(key1, data))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, data))

