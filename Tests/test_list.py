import unittest
import list_id_for_test as lt


class json_search_test(unittest.TestCase):
    def test_list_is_list(self):
        self.assertIsInstance(lt.fetch(lt.items, lt.dictor), list)

    def test_id_is_float(self):
        a = lt.fetch(lt.items, lt.dictor)
        for i in a:
            self.assertIsInstance(i, str)

    def test_subj_is_float(self):
        a = lt.fetch(lt.items, lt.dictor)
        for i in a:
            b = float(i)
            self.assertIsInstance(b, float)


