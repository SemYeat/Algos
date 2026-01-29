import unittest
from lab_7.task5.task_5 import *

class TestLCS(unittest.TestCase):
    """Тесты для функции lcs (наибольшая общая подпоследовательность трех последовательностей)"""

    def test_example1_from_task(self):
        """Тест: пример 1 из задания"""
        arr1 = [1, 2, 3]
        arr2 = [2, 1, 3]
        arr3 = [1, 3, 5]
        result = lcs(arr1, arr2, arr3)
        expected = 2  # (1, 3)
        self.assertEqual(result, expected)

    def test_example2_from_task(self):
        """Тест: пример 2 из задания"""
        arr1 = [8, 3, 2, 1, 7]
        arr2 = [8, 2, 1, 3, 8, 10, 7]
        arr3 = [6, 8, 3, 1, 4, 7]
        result = lcs(arr1, arr2, arr3)
        expected = 3  # (8, 3, 7) или (8, 1, 7)
        self.assertEqual(result, expected)

    def test_identical_sequences(self):
        """Тест: идентичные последовательности"""
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]
        arr3 = [1, 2, 3, 4, 5]
        result = lcs(arr1, arr2, arr3)
        expected = 5
        self.assertEqual(result, expected)

    def test_no_common_subsequence(self):
        """Тест: нет общей подпоследовательности"""
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        arr3 = [7, 8, 9]
        result = lcs(arr1, arr2, arr3)
        expected = 0
        self.assertEqual(result, expected)

    def test_partial_match(self):
        """Тест: частичное совпадение"""
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [3, 4, 5, 6, 7]
        arr3 = [2, 3, 4, 8, 9]
        result = lcs(arr1, arr2, arr3)
        expected = 2  # (3, 4)
        self.assertEqual(result, expected)

    def test_single_common_element(self):
        """Тест: один общий элемент"""
        arr1 = [1, 2, 3]
        arr2 = [3, 4, 5]
        arr3 = [6, 3, 7]
        result = lcs(arr1, arr2, arr3)
        expected = 1  # (3)
        self.assertEqual(result, expected)

    def test_empty_sequences(self):
        """Тест: пустые последовательности"""
        arr1 = []
        arr2 = []
        arr3 = []
        result = lcs(arr1, arr2, arr3)
        expected = 0
        self.assertEqual(result, expected)

    def test_duplicate_elements(self):
        """Тест: повторяющиеся элементы"""
        arr1 = [1, 2, 2, 3]
        arr2 = [2, 2, 3, 4]
        arr3 = [1, 2, 2, 5]
        result = lcs(arr1, arr2, arr3)
        expected = 2  # (2, 2)
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Тест: отрицательные числа"""
        arr1 = [-1, -2, -3]
        arr2 = [-2, -3, -4]
        arr3 = [-1, -2, -3]
        result = lcs(arr1, arr2, arr3)
        expected = 2  # (-2, -3)
        self.assertEqual(result, expected)

    def test_different_lengths(self):
        """Тест: последовательности разной длины"""
        arr1 = [1, 2, 3]
        arr2 = [2, 3, 4, 5]
        arr3 = [3, 4]
        result = lcs(arr1, arr2, arr3)
        expected = 1  # (3)
        self.assertEqual(result, expected)

    def test_large_sequence(self):
        """Тест: большая последовательность"""
        arr1 = list(range(1, 11))  # 1..10
        arr2 = list(range(5, 16))  # 5..15
        arr3 = list(range(8, 19))  # 8..18
        result = lcs(arr1, arr2, arr3)
        expected = 3  # (8, 9, 10)
        self.assertEqual(result, expected)

    def test_zero_sequence(self):
        """Тест: последовательности с нулями"""
        arr1 = [0, 1, 0, 2]
        arr2 = [0, 2, 0, 3]
        arr3 = [0, 1, 0, 3]
        result = lcs(arr1, arr2, arr3)
        expected = 2  # (0, 0)
        self.assertEqual(result, expected)


class TestLimit(unittest.TestCase):
    """Тесты для функции limit"""

    def test_valid_limits(self):
        """Тест: корректные данные"""
        self.assertTrue(limit(3, [1, 2, 3], 3, [4, 5, 6], 3, [7, 8, 9]))
        self.assertTrue(limit(1, [100], 1, [-100], 1, [0]))
        self.assertTrue(limit(100, list(range(100)), 100, list(range(100, 200)), 100, list(range(200, 300))))