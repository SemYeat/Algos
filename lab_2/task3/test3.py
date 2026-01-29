import unittest
from lab_2.task3.task_3 import *


class TestInversionCounter(unittest.TestCase):
    """Тесты для класса InversionCounter"""

    def test_example_from_task(self):
        """Тест: пример из задания"""
        arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        expected = 17  # Как указано в примере
        self.assertEqual(result, expected)

    def test_sorted_array_ascending(self):
        """Тест: отсортированный по возрастанию массив (0 инверсий)"""
        arr = [1, 2, 3, 4, 5]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        expected = 0
        self.assertEqual(result, expected)

    def test_sorted_array_descending(self):
        """Тест: отсортированный по убыванию массив (максимальное число инверсий)"""
        arr = [5, 4, 3, 2, 1]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        # Для 5 элементов: n*(n-1)/2 = 5*4/2 = 10 инверсий
        expected = 10
        self.assertEqual(result, expected)

    def test_simple_array(self):
        """Тест: простой массив"""
        arr = [2, 4, 1, 3, 5]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        # Инверсии: (2,1), (4,1), (4,3) = 3 инверсии
        expected = 3
        self.assertEqual(result, expected)

    def test_array_with_duplicates(self):
        """Тест: массив с повторяющимися элементами"""
        arr = [3, 1, 4, 1, 5]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        # Инверсии: (3,1), (3,1), (4,1) = 3 инверсии
        expected = 3
        self.assertEqual(result, expected)

    def test_single_element(self):
        """Тест: один элемент (0 инверсий)"""
        arr = [42]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        expected = 0
        self.assertEqual(result, expected)

    def test_empty_array(self):
        """Тест: пустой массив (0 инверсий)"""
        arr = []
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        expected = 0
        self.assertEqual(result, expected)

    def test_array_with_negative_numbers(self):
        """Тест: массив с отрицательными числами"""
        arr = [-5, -1, -10, 0, 3]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        # Инверсии: (-5,-10), (-1,-10) = 2 инверсии
        expected = 2
        self.assertEqual(result, expected)

    def test_all_equal_elements(self):
        """Тест: все элементы одинаковые (0 инверсий)"""
        arr = [7, 7, 7, 7]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        expected = 0
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Тест: большие числа (граничные значения)"""
        arr = [1000000000, -1000000000, 999999999, 0]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        # Инверсии: (10^9, -10^9), (10^9, 999999999), (10^9, 0), (999999999, 0) = 4 инверсии
        expected = 4
        self.assertEqual(result, expected)

    def test_formula_for_max_inversions(self):
        """Тест: проверка формулы n*(n-1)/2 для максимального числа инверсий"""
        n = 10
        arr = list(range(n, 0, -1))  # [10, 9, 8, ..., 1]
        counter = InversionCounter()
        result = counter.get_inversion_count(arr)
        expected = n * (n - 1) // 2  # 10*9/2 = 45
        self.assertEqual(result, expected)


class TestLimits(unittest.TestCase):
    """Тесты для функции limits"""

    def test_valid_limits(self):
        """Тест: корректные данные"""
        self.assertTrue(limits(5, [1, 2, 3, 4, 5]))
        self.assertTrue(limits(1, [0]))
        self.assertTrue(limits(100000, [10 ** 9] * 100000))  # Максимальная длина
        self.assertTrue(limits(100000, [-10 ** 9] * 100000))

    def test_invalid_n_too_small(self):
        """Тест: n слишком маленькое"""
        self.assertFalse(limits(0, []))
        self.assertFalse(limits(-1, []))

    def test_invalid_n_too_large(self):
        """Тест: n слишком большое"""
        self.assertFalse(limits(100001, list(range(100001))))

    def test_invalid_numbers_too_large(self):
        """Тест: числа слишком большие"""
        self.assertFalse(limits(1, [10 ** 9 + 1]))
        self.assertFalse(limits(1, [-10 ** 9 - 1]))

    def test_valid_boundary(self):
        """Тест: граничные значения"""
        self.assertTrue(limits(1, [10 ** 9]))
        self.assertTrue(limits(1, [-10 ** 9]))
        self.assertTrue(limits(2, [999999999, -999999999]))