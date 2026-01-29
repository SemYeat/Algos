import unittest
from lab_0.task1.task_1 import add, limits, add_txt

class TestAddFunction(unittest.TestCase):
    """Тесты для функции add()"""

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(0, 0), 0)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(10, -3), 7)

    def test_add_large_numbers(self):
        self.assertEqual(add(10 ** 9, 10 ** 9), 2 * 10 ** 9)
        self.assertEqual(add(-10 ** 9, 10 ** 9), 0)


class TestLimitsFunction(unittest.TestCase):
    """Тесты для функции limits()"""

    def test_within_limits(self):
        self.assertTrue(limits(0, 0))
        self.assertTrue(limits(10 ** 9, 10 ** 9))
        self.assertTrue(limits(-10 ** 9, -10 ** 9))
        self.assertTrue(limits(10 ** 9, -10 ** 9))
        self.assertTrue(limits(999999999, 999999999))

    def test_exceeds_limits(self):
        self.assertFalse(limits(10 ** 9 + 1, 0))
        self.assertFalse(limits(0, 10 ** 9 + 1))
        self.assertFalse(limits(-10 ** 9 - 1, 0))
        self.assertFalse(limits(0, -10 ** 9 - 1))
        self.assertFalse(limits(10 ** 9 + 1, 10 ** 9 + 1))

    def test_boundary_values(self):
        self.assertTrue(limits(10 ** 9, 0))
        self.assertTrue(limits(-10 ** 9, 0))
        self.assertFalse(limits(10 ** 9 + 1, 0))
        self.assertFalse(limits(-10 ** 9 - 1, 0))

if __name__ == '__main__':
    unittest.main()


