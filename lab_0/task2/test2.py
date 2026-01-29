import unittest
from lab_0.task2.task_2 import add_sqrt, limits, add_sqrt_txt
from unittest.mock import mock_open, patch

class TestAddSqrtFunction(unittest.TestCase):
    """Тесты для функции add_sqrt() - a + b**2"""

    def test_add_sqrt_positive_numbers(self):
        self.assertEqual(add_sqrt(2, 3), 2 + 3 * 3)  # 2 + 9 = 11
        self.assertEqual(add_sqrt(5, 2), 5 + 2 * 2)  # 5 + 4 = 9
        self.assertEqual(add_sqrt(0, 5), 0 + 5 * 5)  # 0 + 25 = 25
        self.assertEqual(add_sqrt(10, 0), 10 + 0)  # 10 + 0 = 10

    def test_add_sqrt_negative_numbers(self):
        self.assertEqual(add_sqrt(-2, 3), -2 + 9)  # -2 + 9 = 7
        self.assertEqual(add_sqrt(5, -2), 5 + 4)  # 5 + 4 = 9 (квадрат отрицательного)
        self.assertEqual(add_sqrt(-3, -4), -3 + 16)  # -3 + 16 = 13
        self.assertEqual(add_sqrt(-10, 5), -10 + 25)  # -10 + 25 = 15

    def test_add_sqrt_special_cases(self):
        self.assertEqual(add_sqrt(1, 1), 2)  # 1 + 1 = 2
        self.assertEqual(add_sqrt(100, 10), 200)  # 100 + 100 = 200
        self.assertEqual(add_sqrt(0, 0), 0)  # 0 + 0 = 0
        self.assertEqual(add_sqrt(-1, 0), -1)  # -1 + 0 = -1

    def test_add_sqrt_large_numbers(self):
        self.assertEqual(add_sqrt(10 ** 9, 10 ** 3), 10 ** 9 + 10 ** 6)
        self.assertEqual(add_sqrt(1000, 1000), 1000 + 1000000)  # 1001000


class TestLimitsFunction(unittest.TestCase):
    """Тесты для функции limits()"""

    def test_within_limits(self):
        self.assertTrue(limits(0, 0))
        self.assertTrue(limits(10 ** 9, 10 ** 9))
        self.assertTrue(limits(-10 ** 9, -10 ** 9))
        self.assertTrue(limits(500000000, 500000000))
        self.assertTrue(limits(-10 ** 9, 10 ** 9))

    def test_exceeds_limits(self):
        self.assertFalse(limits(10 ** 9 + 1, 0))
        self.assertFalse(limits(0, 10 ** 9 + 1))
        self.assertFalse(limits(-10 ** 9 - 1, 100))
        self.assertFalse(limits(100, -10 ** 9 - 1))
        self.assertFalse(limits(10 ** 9 + 1, 10 ** 9 + 1))

    def test_boundary_values(self):
        self.assertTrue(limits(10 ** 9, 0))
        self.assertTrue(limits(-10 ** 9, 0))
        self.assertTrue(limits(0, 10 ** 9))
        self.assertTrue(limits(0, -10 ** 9))
        self.assertFalse(limits(10 ** 9 + 1, 0))
        self.assertFalse(limits(0, 10 ** 9 + 1))

    def test_add_sqrt_txt_within_limits(self):
        """Тест с числами в пределах границ"""
        test_input = "3 4\n"  # 3 + 4² = 3 + 16 = 19
        expected_output = "19"

        # Используем mock для файловых операций
        with patch('builtins.open', side_effect=[
            mock_open(read_data=test_input).return_value,  # Для чтения input.txt
            mock_open().return_value  # Для записи output.txt
        ]) as mock_file:
            result = add_sqrt_txt()

            # Проверяем что функция возвращает None (успех)
            self.assertIsNone(result)

            # Проверяем что файлы открывались с правильными параметрами
            mock_file.assert_any_call('input.txt', 'r')
            mock_file.assert_any_call('output.txt', 'w')
