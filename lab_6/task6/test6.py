import unittest
from lab_6.task6.task_6 import *


class TestFibonacciChecker(unittest.TestCase):
    """Тесты для проверки чисел Фибоначчи"""

    def test_perfect_sq_small_numbers(self):
        """Тест: проверка точных квадратов для маленьких чисел"""
        # Точные квадраты
        self.assertTrue(perfect_sq(1))
        self.assertTrue(perfect_sq(4))
        self.assertTrue(perfect_sq(9))
        self.assertTrue(perfect_sq(16))
        self.assertTrue(perfect_sq(25))

        # Не точные квадраты
        self.assertFalse(perfect_sq(2))
        self.assertFalse(perfect_sq(3))
        self.assertFalse(perfect_sq(5))
        self.assertFalse(perfect_sq(7))
        self.assertFalse(perfect_sq(8))

    def test_perfect_sq_large_numbers(self):
        """Тест: проверка точных квадратов для больших чисел"""
        # 10000 = 100^2
        self.assertTrue(perfect_sq(10000))
        # 9801 = 99^2
        self.assertTrue(perfect_sq(9801))
        # 10001 не квадрат
        self.assertFalse(perfect_sq(10001))

    def test_fib_example(self):
        """Тест: пример из задания"""
        # Числа Фибоначчи: 1, 1, 2, 3, 5, 8, 13, ...
        self.assertEqual(fib(1), "Yes")  # F₀ и F₁
        self.assertEqual(fib(2), "Yes")  # F₂
        self.assertEqual(fib(3), "Yes")  # F₃
        self.assertEqual(fib(4), "No")  # не Фибоначчи
        self.assertEqual(fib(5), "Yes")  # F₄
        self.assertEqual(fib(6), "No")  # не Фибоначчи
        self.assertEqual(fib(7), "No")  # не Фибоначчи
        self.assertEqual(fib(8), "Yes")  # F₅

    def test_fib_sequence(self):
        """Тест: последовательность чисел Фибоначчи"""
        # Первые 10 чисел Фибоначчи (согласно определению F₀=F₁=1)
        fib_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        for num in fib_numbers:
            self.assertEqual(fib(num), "Yes", f"{num} должно быть числом Фибоначчи")

        # Некоторые не-числа Фибоначчи
        non_fib_numbers = [4, 6, 7, 9, 10, 11, 12, 14, 15]

        for num in non_fib_numbers:
            self.assertEqual(fib(num), "No", f"{num} НЕ должно быть числом Фибоначчи")

    def test_fib_large_fibonacci(self):
        """Тест: большие числа Фибоначчи"""
        # 89 - число Фибоначчи (F₁₀)
        self.assertEqual(fib(89), "Yes")

        # 144 - число Фибоначчи (F₁₁)
        self.assertEqual(fib(144), "Yes")

        # 987 - число Фибоначчи (F₁₅)
        self.assertEqual(fib(987), "Yes")

        # 1000 - не число Фибоначчи
        self.assertEqual(fib(1000), "No")


class TestLimitFunction(unittest.TestCase):
    """Тесты для функции limit"""

    def test_valid_input(self):
        """Тест: валидные данные"""
        length = 5
        numbers = [1, 2, 3, 4, 5]

        self.assertTrue(limit(length, numbers))

    def test_count_mismatch(self):
        """Тест: несоответствие количества чисел"""
        length = 5
        numbers = [1, 2, 3]  # только 3 числа вместо 5

        self.assertFalse(limit(length, numbers))

    def test_too_many_numbers(self):
        """Тест: слишком много чисел"""
        length = 10 ** 6 + 1
        numbers = list(range(10 ** 6 + 1))

        self.assertFalse(limit(length, numbers))

    def test_empty_numbers(self):
        """Тест: пустой список чисел"""
        length = 0
        numbers = []

        self.assertFalse(limit(length, numbers))  # длина должна быть ≥ 1

    def test_number_too_large(self):
        """Тест: слишком большое число"""
        length = 1
        numbers = [10 ** 5000]  # 10^5000 имеет 5001 цифр

        self.assertFalse(limit(length, numbers))


class TestFibTxtIntegration(unittest.TestCase):
    """Интеграционные тесты для fib_txt"""

    def setUp(self):
        """Настройка для тестов"""
        self.original_stdin = sys.stdin
        self.original_stdout = sys.stdout

    def tearDown(self):
        """Восстановление стандартных потоков"""
        sys.stdin = self.original_stdin
        sys.stdout = self.original_stdout

    def test_example_input(self):
        """Тест: пример из задания"""
        input_data = """8
1
2
3
4
5
6
7
8"""
        expected_output = """Yes
Yes
Yes
No
Yes
No
No
Yes"""