import unittest
from lab_2.task1.task_1 import *


class TestMergeSort(unittest.TestCase):
    """Тесты для функции merge_sort"""

    def test_example_from_task(self):
        """Тест: пример из задания (сортировка по возрастанию)"""
        arr = [31, 41, 59, 26, 41, 58]
        result = merge_sort(arr)
        expected = sorted(arr)  # По возрастанию
        self.assertEqual(result, expected)

    def test_simple_array(self):
        """Тест: простой массив"""
        arr = [5, 2, 8, 1, 9]
        result = merge_sort(arr)
        expected = [1, 2, 5, 8, 9]
        self.assertEqual(result, expected)

    def test_already_sorted_ascending(self):
        """Тест: уже отсортированный по возрастанию массив"""
        arr = [1, 2, 3, 4, 5]
        result = merge_sort(arr)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_reverse_sorted(self):
        """Тест: массив в убывающем порядке (нужно отсортировать по возрастанию)"""
        arr = [5, 4, 3, 2, 1]
        result = merge_sort(arr)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_with_negative_numbers(self):
        """Тест: с отрицательными числами"""
        arr = [-5, -1, -10, 0, 3]
        result = merge_sort(arr)
        expected = [-10, -5, -1, 0, 3]
        self.assertEqual(result, expected)

    def test_single_element(self):
        """Тест: один элемент"""
        arr = [42]
        result = merge_sort(arr)
        expected = [42]
        self.assertEqual(result, expected)

    def test_empty_array(self):
        """Тест: пустой массив"""
        arr = []
        result = merge_sort(arr)
        expected = []
        self.assertEqual(result, expected)

    def test_duplicates(self):
        """Тест: повторяющиеся элементы"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = merge_sort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Тест: большие числа (граничные значения)"""
        arr = [1000000000, -1000000000, 999999999, 0]
        result = merge_sort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)

    def test_all_equal_elements(self):
        """Тест: все элементы одинаковые"""
        arr = [7, 7, 7, 7]
        result = merge_sort(arr)
        expected = [7, 7, 7, 7]
        self.assertEqual(result, expected)

    def test_large_array(self):
        """Тест: большой массив (проверка рекурсии)"""
        arr = list(range(1000, 0, -1))  # 1000 элементов в обратном порядке
        result = merge_sort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)

    def test_odd_length(self):
        """Тест: массив нечетной длины"""
        arr = [3, 1, 4, 1, 5]
        result = merge_sort(arr)
        expected = [1, 1, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_even_length(self):
        """Тест: массив четной длины"""
        arr = [3, 1, 4, 1]
        result = merge_sort(arr)
        expected = [1, 1, 3, 4]
        self.assertEqual(result, expected)


class TestMergeFunction(unittest.TestCase):
    """Тесты для функции merge"""

    def test_merge_simple(self):
        """Тест: простое слияние"""
        left = [1, 3, 5]
        right = [2, 4, 6]
        result = merge(left, right)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected)

    def test_merge_left_empty(self):
        """Тест: слияние с пустым левым массивом"""
        left = []
        right = [2, 4, 6]
        result = merge(left, right)
        expected = [2, 4, 6]
        self.assertEqual(result, expected)

    def test_merge_right_empty(self):
        """Тест: слияние с пустым правым массивом"""
        left = [1, 3, 5]
        right = []
        result = merge(left, right)
        expected = [1, 3, 5]
        self.assertEqual(result, expected)

    def test_merge_with_duplicates(self):
        """Тест: слияние с дубликатами"""
        left = [1, 2, 2, 3]
        right = [2, 3, 4]
        result = merge(left, right)
        expected = [1, 2, 2, 2, 3, 3, 4]
        self.assertEqual(result, expected)

    def test_merge_different_lengths(self):
        """Тест: слияние массивов разной длины"""
        left = [1, 3, 5, 7, 9]
        right = [2, 4, 6]
        result = merge(left, right)
        expected = [1, 2, 3, 4, 5, 6, 7, 9]
        self.assertEqual(result, expected)

    def test_merge_negative_numbers(self):
        """Тест: слияние с отрицательными числами"""
        left = [-5, -1, 0]
        right = [-3, 2, 4]
        result = merge(left, right)
        expected = [-5, -3, -1, 0, 2, 4]
        self.assertEqual(result, expected)