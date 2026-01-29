import unittest
from lab_3.task1.task_1 import *

class TestQuickSort(unittest.TestCase):
    """Тесты для функции quick_sort"""

    def test_empty_array(self):
        """Тест: пустой массив"""
        result = quick_sort([])
        expected = []
        self.assertEqual(result, expected)

    def test_single_element(self):
        """Тест: один элемент"""
        result = quick_sort([42])
        expected = [42]
        self.assertEqual(result, expected)

    def test_sorted_array(self):
        """Тест: уже отсортированный массив"""
        array = [1, 2, 3, 4, 5]
        result = quick_sort(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

    def test_reverse_sorted(self):
        """Тест: обратно отсортированный массив"""
        array = [5, 4, 3, 2, 1]
        result = quick_sort(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

    def test_random_array(self):
        """Тест: случайный массив"""
        array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = quick_sort(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

    def test_duplicate_elements(self):
        """Тест: повторяющиеся элементы"""
        array = [5, 2, 8, 2, 5, 1, 8]
        result = quick_sort(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Тест: отрицательные числа"""
        array = [-5, -1, -10, 0, 3]
        result = quick_sort(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

    def test_all_equal_elements(self):
        """Тест: все элементы одинаковые"""
        array = [7, 7, 7, 7, 7]
        result = quick_sort(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Тест: большие числа"""
        array = [1000000000, -1000000000, 999999999, 0]
        result = quick_sort(array)
        expected = sorted(array)
        self.assertEqual(result, expected)

class TestLimit(unittest.TestCase):
    """Тесты для функции limit"""

    def test_valid_limits(self):
        """Тест: корректные данные"""
        self.assertTrue(limit(5, [1, 2, 3, 4, 5]))
        self.assertTrue(limit(1, [0]))
        self.assertTrue(limit(10000, list(range(10000))))  # Максимальный размер
        self.assertTrue(limit(3, [-10 ** 9, 0, 10 ** 9]))  # Граничные значения

    def test_invalid_n_too_small(self):
        """Тест: n слишком маленькое"""
        self.assertFalse(limit(0, []))

    def test_invalid_n_too_large(self):
        """Тест: n слишком большое"""
        self.assertFalse(limit(10001, list(range(10001))))

    def test_invalid_array_length(self):
        """Тест: длина массива не равна n"""
        self.assertFalse(limit(5, [1, 2, 3]))  # Короче
        self.assertFalse(limit(3, [1, 2, 3, 4]))  # Длиннее