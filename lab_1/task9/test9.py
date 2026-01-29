import unittest
from lab_1.task9.task_9 import *


class TestBinaryAddition(unittest.TestCase):
    """Тесты для функции binary_add"""
    def test_simple_addition(self):
        """Тест: простое сложение"""
        result = binary_add("01", "01")  # 1 + 1 = 2
        expected = "10"  # 2 в двоичной
        self.assertEqual(result, expected)

    def test_addition_with_carry(self):
        """Тест: сложение с переносом"""
        result = binary_add("11", "01")  # 3 + 1 = 4
        expected = "100"  # 4 в двоичной
        self.assertEqual(result, expected)

    def test_addition_no_carry(self):
        """Тест: сложение без переноса"""
        result = binary_add("10", "01")  # 2 + 1 = 3
        expected = "11"  # 3 в двоичной
        self.assertEqual(result, expected)

    def test_addition_large_numbers(self):
        """Тест: сложение больших чисел"""
        result = binary_add("1111", "0001")  # 15 + 1 = 16
        expected = "10000"  # 16 в двоичной
        self.assertEqual(result, expected)

    def test_addition_with_multiple_carries(self):
        """Тест: сложение с несколькими переносами"""
        result = binary_add("111", "001")  # 7 + 1 = 8
        expected = "1000"  # 8 в двоичной
        self.assertEqual(result, expected)

    def test_addition_zero(self):
        """Тест: сложение с нулем"""
        result = binary_add("000", "000")  # 0 + 0 = 0
        expected = "0"  # Убираем ведущие нули
        self.assertEqual(result, expected)

    def test_addition_max_bits(self):
        """Тест: сложение чисел из всех единиц"""
        result = binary_add("111", "111")  # 7 + 7 = 14
        expected = "1110"  # 14 в двоичной
        self.assertEqual(result, expected)

    def test_addition_different_patterns(self):
        """Тест: сложение с разными паттернами"""
        result = binary_add("1010", "0101")  # 10 + 5 = 15
        expected = "1111"  # 15 в двоичной
        self.assertEqual(result, expected)

    def test_addition_single_bit(self):
        """Тест: сложение однобитных чисел"""
        result = binary_add("1", "1")  # 1 + 1 = 2
        expected = "10"  # 2 в двоичной
        self.assertEqual(result, expected)

    def test_addition_with_leading_zeros(self):
        """Тест: сложение чисел с ведущими нулями"""
        result = binary_add("001", "010")  # 1 + 2 = 3
        expected = "11"  # 3 в двоичной (ведущие нули убраны)
        self.assertEqual(result, expected)


class TestLimit(unittest.TestCase):
    """Тесты для функции limit"""

    def test_valid_limits(self):
        """Тест: корректные данные"""
        self.assertTrue(limit("101", "110"))  # Одинаковая длина, только 0 и 1
        self.assertTrue(limit("1", "0"))  # Минимальная длина
        self.assertTrue(limit("0" * 1000, "1" * 1000))  # Максимальная длина

    def test_invalid_length_too_small(self):
        """Тест: длина слишком маленькая"""
        self.assertFalse(limit("", ""))  # Пустые строки
        self.assertFalse(limit("", "1"))  # Одна пустая строка

    def test_invalid_length_too_large(self):
        """Тест: длина слишком большая"""
        long_str = "1" * 1001  # 1001 бит
        self.assertFalse(limit(long_str, long_str))

    def test_invalid_different_lengths(self):
        """Тест: числа разной длины"""
        self.assertFalse(limit("101", "10"))  # 3 бита и 2 бита
        self.assertFalse(limit("1", "10"))  # 1 бит и 2 бита

    def test_invalid_characters(self):
        """Тест: недопустимые символы"""
        self.assertFalse(limit("102", "101"))  # Цифра 2
        self.assertFalse(limit("10a", "101"))  # Буква a
        self.assertFalse(limit("101", "10-"))  # Символ -
        self.assertFalse(limit("1 0", "101"))  # Пробел

    def test_valid_boundary_values(self):
        """Тест: граничные значения"""
        self.assertTrue(limit("0", "1"))  # Минимальная длина
        self.assertTrue(limit("1", "1"))  # Минимальная длина, одинаковые
        long_valid = "1" * 1000  # 1000 бит
        self.assertTrue(limit(long_valid, "0" * 1000))

    def test_all_zeros_and_ones(self):
        """Тест: все нули и все единицы"""
        self.assertTrue(limit("0000", "1111"))
        self.assertTrue(limit("1111", "0000"))
        self.assertTrue(limit("0101", "1010"))