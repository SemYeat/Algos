import unittest
from lab_0.task4.task_4 import add_fib_txt, multipl, matr_multipl, limits, fib_num

class TestFibonacciFunctions(unittest.TestCase):
    """Тесты для функций вычисления последней цифры Фибоначчи"""

    def test_fib_num(self):
        """Тест малых чисел Фибоначчи"""
        self.assertEqual(fib_num(0), 0)
        self.assertEqual(fib_num(1), 1)
        self.assertEqual(fib_num(2), 1)
        self.assertEqual(fib_num(3), 2)
        self.assertEqual(fib_num(4), 3)
        self.assertEqual(fib_num(5), 5)
        self.assertEqual(fib_num(6), 8)
        self.assertEqual(fib_num(7), 3)  # 13 → 3
        self.assertEqual(fib_num(8), 1)  # 21 → 1
        self.assertEqual(fib_num(9), 4)  # 34 → 4
        self.assertEqual(fib_num(10), 5)  # 55 → 5
        self.assertEqual(fib_num(20), 5)  # 6765 → 5

    def test_fib_num_from_task(self):
        """Тест примеров из задания"""
        self.assertEqual(fib_num(331), 9)
        self.assertEqual(fib_num(327305), 5)

    def test_limits(self):
        """Тест функции limits для значений в пределах диапазона"""
        self.assertTrue(limits(0))
        self.assertTrue(limits(1))
        self.assertTrue(limits(5000000))
        self.assertTrue(limits(10 ** 7))
        self.assertTrue(limits(10 ** 7 - 1))

    def test_limits_outof_range(self):
        """Тест функции limits для значений вне диапазона"""
        self.assertFalse(limits(-1))
        self.assertFalse(limits(10 ** 7 + 1))
        self.assertFalse(limits(10 ** 8))
        self.assertFalse(limits(-100))


    def test_multipl_base_cases(self):
        """Тест возведения матрицы в степень для базовых случаев"""
        # M^0 должна быть единичной матрицей
        result0 = multipl([[0, 1], [1, 1]], 0)
        self.assertEqual(result0, [[1, 0], [0, 1]])

        # M^1 должна быть исходной матрицей
        result1 = multipl([[0, 1], [1, 1]], 1)
        self.assertEqual(result1[0][0], 0)
        self.assertEqual(result1[0][1], 1)
        self.assertEqual(result1[1][0], 1)
        self.assertEqual(result1[1][1], 1)

    def test_matr_multipl(self):
        """Тест умножения матриц с учетом модуля 10"""
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]

        # (1*5 + 2*7, 1*6 + 2*8) = (19, 22) → (9, 2) по модулю 10
        # (3*5 + 4*7, 3*6 + 4*8) = (43, 50) → (3, 0) по модулю 10
        result = matr_multipl(A, B)

        # Проверяем значения с учетом модуля 10
        self.assertEqual(result[0][0], 9)  # 19 % 10 = 9
        self.assertEqual(result[0][1], 2)  # 22 % 10 = 2
        self.assertEqual(result[1][0], 3)  # 43 % 10 = 3
        self.assertEqual(result[1][1], 0)  # 50 % 10 = 0

    def test_matr_multipl_fib_matrix(self):
        """Тест умножения матрицы Фибоначчи на себя"""
        fib_matrix = [[0, 1], [1, 1]]

        # F^2 = [[1, 1], [1, 2]]
        result = matr_multipl(fib_matrix, fib_matrix)

        # Проверяем значения
        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[0][1], 1)
        self.assertEqual(result[1][0], 1)
        self.assertEqual(result[1][1], 2)