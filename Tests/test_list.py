import unittest
import list_id_for_test as lt


class json_search_test(unittest.TestCase):
    def test_list_is_list(self):
        self.assertIsInstance(lt.dictor, list)

    def test_id_is_float(self):
        for i in range(0, len(lt.dictor)-1):
            self.assertIs(float(lt.dictor[i]), float)

    def test_is_a_list(self):
        list_float = [float(i) for i in lt.fetch(lt.items, lt.dictor)]
        self.assertIs(list_float[1], float)

