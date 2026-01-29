import unittest
from lab_7.task1.task_1 import *

class TestExchange(unittest.TestCase):
    """Тесты для функции exchange (неограниченное количество монет)"""

    def test_example_from_task(self):
        """Тест: пример из задания (1, 3, 4)"""
        result = exchange(6, [1, 3, 4])
        expected = 2  # 3 + 3
        self.assertEqual(result, expected)

    def test_simple_exchange(self):
        """Тест: простой размен"""
        result = exchange(5, [1, 2, 5])
        expected = 1  # 5
        self.assertEqual(result, expected)

    def test_exact_change(self):
        """Тест: точный размен"""
        result = exchange(10, [2, 5, 10])
        expected = 1  # 10
        self.assertEqual(result, expected)

    def test_multiple_coins_needed(self):
        """Тест: требуется несколько монет"""
        result = exchange(13, [1, 4, 5])
        expected = 3  # 5 + 4 + 4
        self.assertEqual(result, expected)

    def test_no_possible_change(self):
        """Тест: размен невозможен"""
        result = exchange(5, [2, 4])
        expected = -1  # Невозможно разменять
        self.assertEqual(result, expected)

    def test_zero_money(self):
        """Тест: сумма 0"""
        result = exchange(0, [1, 3, 4])
        expected = 0  # 0 монет
        self.assertEqual(result, expected)

    def test_single_coin_type(self):
        """Тест: один тип монет"""
        result = exchange(7, [2])
        expected = -1  # Невозможно разменять нечетную сумму монетами по 2
        self.assertEqual(result, expected)

    def test_all_ones(self):
        """Тест: все монеты по 1"""
        result = exchange(10, [1])
        expected = 10  # 10 монет по 1
        self.assertEqual(result, expected)

    def test_optimal_not_greedy(self):
        """Тест: случай, когда жадный алгоритм не оптимален"""
        result = exchange(30, [1, 10, 25])
        expected = 3  # 10 + 10 + 10 (жадный дал бы 25 + 1 + 1 + 1 + 1 + 1)
        self.assertEqual(result, expected)

    def test_large_money(self):
        """Тест: большая сумма"""
        result = exchange(100, [1, 5, 10, 25, 50])
        expected = 2  # 50 + 50
        self.assertEqual(result, expected)


class TestExchangeLimited(unittest.TestCase):
    """Тесты для функции exchange_limited (ограниченное количество монет)"""

    def test_sufficient_coins(self):
        """Тест: достаточно монет"""
        result = exchange_limited(6, [1, 3, 4], [10, 10, 10])
        expected = 2  # 3 + 3
        self.assertEqual(result, expected)

    def test_limited_coins_available(self):
        """Тест: ограниченное количество монет доступно"""
        result = exchange_limited(6, [1, 3, 4], [10, 1, 10])  # Только 1 монета номиналом 3
        expected = 2  # 3 + 3 (есть только одна монета 3, но можно 4+1+1)
        self.assertEqual(result, expected)

    def test_not_enough_coins(self):
        """Тест: недостаточно монет"""
        result = exchange_limited(10, [1, 5], [3, 1])  # Только 1 монета номиналом 5
        expected = 6  # 5 + 1 + 1 + 1 + 1 + 1
        self.assertEqual(result, expected)

    def test_no_coins_of_type(self):
        """Тест: нет монет определенного номинала"""
        result = exchange_limited(6, [1, 3, 4], [10, 0, 10])  # Нет монет номиналом 3
        expected = 2  # 4 + 1 + 1
        self.assertEqual(result, expected)

    def test_exact_with_limits(self):
        """Тест: точный размен с ограничениями"""
        result = exchange_limited(15, [5, 10], [2, 1])  # 2 пятерки и 1 десятка
        expected = 2  # 10 + 5
        self.assertEqual(result, expected)

    def test_impossible_with_limits(self):
        """Тест: невозможен размен из-за ограничений"""
        result = exchange_limited(8, [3, 5], [2, 1])  # 2 тройки и 1 пятерка
        expected = -1  # Невозможно разменять
        self.assertEqual(result, expected)

    def test_zero_counts(self):
        """Тест: нулевые количества монет"""
        result = exchange_limited(5, [1, 2, 5], [0, 0, 1])
        expected = 1  # 5
        self.assertEqual(result, expected)

    def test_use_all_coins(self):
        """Тест: использование всех доступных монет"""
        result = exchange_limited(6, [1, 2], [3, 2])  # 3 единицы и 2 двойки
        expected = 3  # 2 + 2 + 2 (но у нас только 2 двойки) -> 2 + 2 + 1 + 1
        self.assertEqual(result, expected)


class TestLimits(unittest.TestCase):
    """Тесты для функции limits"""

    def test_valid_limits(self):
        """Тест: корректные данные"""
        self.assertTrue(limits(100, 3, [1, 3, 4]))
        self.assertTrue(limits(1, 1, [1]))
        self.assertTrue(limits(1000, 100, list(range(1, 101))))  # Максимальные значения
