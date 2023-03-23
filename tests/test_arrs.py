from utils import arrs
import unittest

class TestArrs(unittest.TestCase):
    def test_arrs(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

        self.assertEqual(arrs.my_slice([], 1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1), [3])
