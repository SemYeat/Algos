import unittest
from lab_2.task8.task_8 import *


class TestKarlMultiply(unittest.TestCase):
    """Тесты для функции karl_multiply"""

    def test_example_from_task(self):
        """Тест: пример из задания"""
        A = [3, 2, 5]  # 3x² + 2x + 5
        B = [5, 1, 2]  # 5x² + x + 2
        result = karl_multiply(A, B)
        expected = [15, 13, 33, 9, 10]  # 15x⁴ + 13x³ + 33x² + 9x + 10
        self.assertEqual(result, expected)

    def test_simple_polynomials(self):
        """Тест: простые многочлены"""
        A = [1, 1]  # x + 1
        B = [1, 1]  # x + 1
        result = karl_multiply(A, B)
        expected = [1, 2, 1]  # x² + 2x + 1
        self.assertEqual(result, expected)

    def test_single_coefficient(self):
        """Тест: один коэффициент (константа)"""
        A = [5]  # 5
        B = [3]  # 3
        result = karl_multiply(A, B)
        expected = [15]  # 15
        self.assertEqual(result, expected)

    def test_zero_polynomial(self):
        """Тест: нулевой многочлен"""
        A = [0, 0, 0]  # 0
        B = [1, 2, 3]  # x² + 2x + 3
        result = karl_multiply(A, B)
        expected = [0, 0, 0, 0, 0]  # 0
        self.assertEqual(result, expected)

    def test_linear_polynomials(self):
        """Тест: линейные многочлены"""
        A = [2, 3]  # 2x + 3
        B = [4, 5]  # 4x + 5
        result = karl_multiply(A, B)
        expected = [8, 22, 15]  # 8x² + 22x + 15
        self.assertEqual(result, expected)

    def test_different_lengths(self):
        """Тест: многочлены разной длины"""
        A = [1, 2, 3]  # x² + 2x + 3
        B = [4, 5]  # 4x + 5
        result = karl_multiply(A, B)
        expected = [4, 13, 22, 15]  # 4x³ + 13x² + 22x + 15
        self.assertEqual(result, expected)

    def test_negative_coefficients(self):
        """Тест: отрицательные коэффициенты"""
        A = [1, -1]  # x - 1
        B = [1, 1]  # x + 1
        result = karl_multiply(A, B)
        expected = [1, 0, -1]  # x² - 1
        self.assertEqual(result, expected)