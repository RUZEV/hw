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


