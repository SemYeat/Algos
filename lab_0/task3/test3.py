import unittest
from lab_0.task3.task_3 import matr_multipl, multipl, fib_num, limits, add_fib_txt


class TestFibonacciFirstTask(unittest.TestCase):
    """Тесты для вычисление полного числа Фибоначчи"""

    def test_fib_num_small_values(self):
        """Тест малых чисел Фибоначчи (полные значения)"""
        self.assertEqual(fib_num(0), 0)
        self.assertEqual(fib_num(1), 1)
        self.assertEqual(fib_num(2), 1)
        self.assertEqual(fib_num(3), 2)
        self.assertEqual(fib_num(4), 3)
        self.assertEqual(fib_num(5), 5)
        self.assertEqual(fib_num(6), 8)
        self.assertEqual(fib_num(7), 13)
        self.assertEqual(fib_num(8), 21)
        self.assertEqual(fib_num(9), 34)
        self.assertEqual(fib_num(10), 55)
        self.assertEqual(fib_num(11), 89)
        self.assertEqual(fib_num(12), 144)

    def test_fib_num_boundary_values(self):
        """Тест первого задания (n <= 45)"""
        self.assertEqual(fib_num(0), 0)
        self.assertEqual(fib_num(45), 1134903170)  # F(45)

        # Проверим несколько промежуточных значений
        self.assertEqual(fib_num(20), 6765)
        self.assertEqual(fib_num(30), 832040)
        self.assertEqual(fib_num(40), 102334155)

    def test_limits_first_task(self):
        """Тест функции limits для первого задания (0 <= n <=45)"""
        # В пределах диапазона
        self.assertTrue(limits(0))
        self.assertTrue(limits(1))
        self.assertTrue(limits(20))
        self.assertTrue(limits(45))
        self.assertTrue(limits(22))  # произвольное значение в диапазоне

        # Вне диапазона
        self.assertFalse(limits(-1))
        self.assertFalse(limits(46))
        self.assertFalse(limits(100))
        self.assertFalse(limits(1000000))

    def test_multipl_base_cases_no_mod(self):
        """Тест возведения матрицы в степень (без модуля)"""
        # M^0 должна быть единичной матрицей
        result0 = multipl([[0, 1], [1, 1]], 0)
        self.assertEqual(result0, [[1, 0], [0, 1]])

        # M^1 должна быть исходной матрицей
        result1 = multipl([[0, 1], [1, 1]], 1)
        self.assertEqual(result1, [[0, 1], [1, 1]])

        # M^2
        result2 = multipl([[0, 1], [1, 1]], 2)
        self.assertEqual(result2, [[1, 1], [1, 2]])

        # M^3
        result3 = multipl([[0, 1], [1, 1]], 3)
        self.assertEqual(result3, [[1, 2], [2, 3]])

    def test_matr_multipl_no_mod(self):
        """Тест умножения матриц (без модуля 10)"""
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]

        # (1*5 + 2*7, 1*6 + 2*8) = (19, 22)
        # (3*5 + 4*7, 3*6 + 4*8) = (43, 50)
        result = matr_multipl(A, B)

        self.assertEqual(result[0][0], 19)
        self.assertEqual(result[0][1], 22)
        self.assertEqual(result[1][0], 43)
        self.assertEqual(result[1][1], 50)