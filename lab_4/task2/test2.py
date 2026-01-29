import unittest
from lab_4.task2.task_2 import *


class TestQueueAct(unittest.TestCase):
    """Тесты для функции queue_act"""

    def test_simple_example(self):
        """Тест: простой пример из задания"""
        actions = ["+ 1", "+ 10", "-"]
        result = queue_act(actions)
        expected = ["1"]
        self.assertEqual(result, expected)

    def test_multiple_enqueue_dequeue(self):
        """Тест: несколько добавлений и удалений"""
        actions = ["+ 1", "+ 2", "+ 3", "-", "-", "+ 4", "-", "-"]
        result = queue_act(actions)
        expected = ["1", "2", "3", "4"]
        self.assertEqual(result, expected)

    def test_fifo_order(self):
        """Тест: проверка порядка FIFO (First In, First Out)"""
        actions = ["+ 5", "+ 3", "+ 7", "-", "-", "-"]
        result = queue_act(actions)
        expected = ["5", "3", "7"]  # Первый вошел - первый вышел
        self.assertEqual(result, expected)

    def test_only_dequeue(self):
        """Тест: только операции удаления"""
        # Сначала добавим элементы, потом удалим все
        actions = ["+ 10", "+ 20", "+ 30", "-", "-", "-"]
        result = queue_act(actions)
        expected = ["10", "20", "30"]
        self.assertEqual(result, expected)

    def test_mixed_operations(self):
        """Тест: смешанные операции"""
        actions = ["+ 1", "-", "+ 2", "+ 3", "-", "+ 4", "-", "-"]
        result = queue_act(actions)
        expected = ["1", "2", "3", "4"]
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Тест: большие числа"""
        actions = ["+ 1000000000", "+ -1000000000", "-", "-"]
        result = queue_act(actions)
        expected = ["1000000000", "-1000000000"]
        self.assertEqual(result, expected)

    def test_empty_actions(self):
        """Тест: пустой список действий"""
        actions = []
        result = queue_act(actions)
        expected = []
        self.assertEqual(result, expected)

    def test_only_enqueue(self):
        """Тест: только добавление, без удаления"""
        actions = ["+ 1", "+ 2", "+ 3"]
        result = queue_act(actions)
        expected = []  # Нет операций удаления
        self.assertEqual(result, expected)

    def test_complex_scenario(self):
        """Тест: сложный сценарий"""
        actions = [
            "+ 100", "-", "+ 200", "+ 300", "-",
            "+ 400", "-", "+ 500", "-", "-"
        ]
        result = queue_act(actions)
        expected = ["100", "200", "300", "400", "500"]
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Тест: отрицательные числа"""
        actions = ["+ -5", "+ -3", "-", "+ -7", "-", "-"]
        result = queue_act(actions)
        expected = ["-5", "-3", "-7"]
        self.assertEqual(result, expected)

    def test_multiple_consecutive_dequeues(self):
        """Тест: несколько удалений подряд"""
        actions = ["+ 1", "+ 2", "+ 3", "-", "-", "-", "+ 4", "-"]
        result = queue_act(actions)
        expected = ["1", "2", "3", "4"]
        self.assertEqual(result, expected)


class TestLimitFunction(unittest.TestCase):
    """Тесты для функции limit"""

    def test_valid_input(self):
        """Тест: ok данные"""
        act_count = 3
        actions = ["+ 1", "+ 2", "-"]
        self.assertTrue(limit(act_count, actions))

    def test_count_mismatch(self):
        """Тест: несоответствие количества действий"""
        act_count = 5
        actions = ["+ 1", "+ 2", "-"]  # только 3 действия вместо 5
        self.assertFalse(limit(act_count, actions))