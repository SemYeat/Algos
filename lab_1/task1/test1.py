import unittest
from lab_1.task1.task_1 import insertion_sort, limits, add_sort_txt


class TestInsertionSort(unittest.TestCase):
    """Тесты для функции insertion_sort"""

    def test_example_from_task(self):
        """Тест: пример из задания"""
        arr = [31, 41, 59, 26, 41, 58]
        result = insertion_sort(6, arr)
        expected = [26, 31, 41, 41, 58, 59]
        self.assertEqual(result, expected)

    def test_simple_array(self):
        """Тест: простой массив"""
        arr = [5, 2, 8, 1, 9]
        result = insertion_sort(5, arr)
        expected = [1, 2, 5, 8, 9]
        self.assertEqual(result, expected)

    def test_already_sorted(self):
        """Тест: уже отсортированный массив"""
        arr = [1, 2, 3, 4, 5]
        result = insertion_sort(5, arr)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_reverse_sorted(self):
        """Тест: массив в обратном порядке"""
        arr = [5, 4, 3, 2, 1]
        result = insertion_sort(5, arr)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_with_negative_numbers(self):
        """Тест: с отрицательными числами"""
        arr = [-5, -1, -10, 0, 3]
        result = insertion_sort(5, arr)
        expected = [-10, -5, -1, 0, 3]
        self.assertEqual(result, expected)

    def test_single_element(self):
        """Тест: один элемент"""
        arr = [42]
        result = insertion_sort(1, arr)
        expected = [42]
        self.assertEqual(result, expected)

    def test_empty_array(self):
        """Тест: пустой массив"""
        arr = []
        result = insertion_sort(0, arr)
        expected = []
        self.assertEqual(result, expected)

    def test_duplicates(self):
        """Тест: повторяющиеся элементы"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = insertion_sort(9, arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Тест: большие числа (граничные значения)"""
        arr = [1000000000, -1000000000, 999999999, 0]
        result = insertion_sort(4, arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)


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

    def test_invalid_numbers_too_large(self):
        """Тест: числа слишком большие"""
        self.assertFalse(limits(1, [10 ** 9 + 1]))
        self.assertFalse(limits(1, [-10 ** 9 - 1]))

    def test_valid_boundary(self):
        """Тест: граничные значения"""
        self.assertTrue(limits(1, [10 ** 9]))
        self.assertTrue(limits(1, [-10 ** 9]))
        self.assertTrue(limits(1000, [999999999, -999999999]))