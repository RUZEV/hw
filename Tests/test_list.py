import unittest
import list_id_for_test as lt


class json_search_test(unittest.TestCase):
    def test_id_is_float(self):
        for i in range(0, len(lt.dictor)-1):
            self.assertEqual(float(lt.dictor[i]), float)