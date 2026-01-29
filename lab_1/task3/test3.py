import unittest
from lab_1.task3.task_3 import *

class TestInsertionSortDescending(unittest.TestCase):
    """Тесты для функции insertion_sort (по убыванию)"""

    def test_example_from_task_descending(self):
        """Тест: пример из задания - сортировка по убыванию"""
        arr = [31, 41, 59, 26, 41, 58]
        result = insertion_sort(6, arr)
        # Ожидаем сортировку по УБЫВАНИЮ
        expected = [59, 58, 41, 41, 31, 26]
        self.assertEqual(result, expected)

    def test_simple_array_descending(self):
        """Тест: простой массив - сортировка по убыванию"""
        arr = [5, 2, 8, 1, 9]
        result = insertion_sort(5, arr)
        expected = [9, 8, 5, 2, 1]  # По убыванию
        self.assertEqual(result, expected)

    def test_already_sorted_descending(self):
        """Тест: уже отсортированный по убыванию массив"""
        arr = [5, 4, 3, 2, 1]
        result = insertion_sort(5, arr)
        expected = [5, 4, 3, 2, 1]  # Остается без изменений
        self.assertEqual(result, expected)

    def test_reverse_sorted_descending(self):
        """Тест: массив в возрастающем порядке (нужно отсортировать по убыванию)"""
        arr = [1, 2, 3, 4, 5]
        result = insertion_sort(5, arr)
        expected = [5, 4, 3, 2, 1]  # Сортировка по убыванию
        self.assertEqual(result, expected)

    def test_with_negative_numbers_descending(self):
        """Тест: с отрицательными числами - сортировка по убыванию"""
        arr = [-5, -1, -10, 0, 3]
        result = insertion_sort(5, arr)
        expected = [3, 0, -1, -5, -10]  # По убыванию
        self.assertEqual(result, expected)

    def test_single_element_descending(self):
        """Тест: один элемент"""
        arr = [42]
        result = insertion_sort(1, arr)
        expected = [42]
        self.assertEqual(result, expected)

    def test_empty_array_descending(self):
        """Тест: пустой массив"""
        arr = []
        result = insertion_sort(0, arr)
        expected = []
        self.assertEqual(result, expected)

    def test_duplicates_descending(self):
        """Тест: повторяющиеся элементы - сортировка по убыванию"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = insertion_sort(9, arr)
        expected = sorted(arr, reverse=True)  # По убыванию
        self.assertEqual(result, expected)

    def test_large_numbers_descending(self):
        """Тест: большие числа - сортировка по убыванию"""
        arr = [1000000000, -1000000000, 999999999, 0]
        result = insertion_sort(4, arr)
        expected = sorted(arr, reverse=True)  # По убыванию
        self.assertEqual(result, expected)

    def test_all_equal_elements(self):
        """Тест: все элементы одинаковые"""
        arr = [7, 7, 7, 7]
        result = insertion_sort(4, arr)
        expected = [7, 7, 7, 7]  # Остаются без изменений
        self.assertEqual(result, expected)

    def test_swap_function(self):
        """Тест: проверка функции swap"""
        a, b = 5, 10
        result_a, result_b = swap(a, b)
        self.assertEqual(result_a, 10)
        self.assertEqual(result_b, 5)


class TestLimits(unittest.TestCase):
    """Тесты для функции limits"""

    def test_valid_limits(self):
        """Тест: корректные данные"""
        self.assertTrue(limits(5, [1, 2, 3, 4, 5]))
        self.assertTrue(limits(1, [0]))
        self.assertTrue(limits(1000, [10 ** 9] * 1000))
        self.assertTrue(limits(1000, [-10 ** 9] * 1000))

    def test_invalid_n_too_small(self):
        """Тест: n слишком маленькое"""
        self.assertFalse(limits(0, []))

    def test_invalid_n_too_large(self):
        """Тест: n слишком большое"""
        self.assertFalse(limits(1001, list(range(1001))))