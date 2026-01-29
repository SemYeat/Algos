import unittest
from lab_4.task6.task_6 import *

class TestQueueAct(unittest.TestCase):
    """Тесты для функции queue_act"""

    def test_example_from_task(self):
        """Тест: пример из задания"""
        actions = ["+ 1", "?", "+ 10", "?", "-", "?", "-"]
        result = queue_act(actions)
        expected = [1, 1, 10]
        self.assertEqual(result, expected)

    def test_simple_minimum(self):
        """Тест: простой поиск минимума"""
        actions = ["+ 5", "+ 3", "+ 7", "?", "-", "?"]
        result = queue_act(actions)
        expected = [3, 3]  # Минимум 3, после удаления 5 минимум остается 3
        self.assertEqual(result, expected)

    def test_minimum_changes_after_removal(self):
        """Тест: минимум меняется после удаления"""
        actions = ["+ 1", "+ 2", "+ 3", "?", "-", "?"]
        result = queue_act(actions)
        expected = [1, 2]  # После удаления 1, минимум становится 2
        self.assertEqual(result, expected)

    def test_multiple_same_minimum(self):
        """Тест: несколько одинаковых минимумов"""
        actions = ["+ 5", "+ 5", "+ 5", "?", "-", "?", "-", "?"]
        result = queue_act(actions)
        expected = [5, 5, 5]  # Все минимумы равны 5
        self.assertEqual(result, expected)

    def test_minimum_with_negative_numbers(self):
        """Тест: отрицательные числа как минимум"""
        actions = ["+ 10", "+ -5", "+ 3", "?", "-", "?"]
        result = queue_act(actions)
        expected = [-5, -5]  # Минимум -5
        self.assertEqual(result, expected)

    def test_minimum_update_on_new_smaller_element(self):
        """Тест: обновление минимума при добавлении меньшего элемента"""
        actions = ["+ 10", "+ 5", "?", "+ 1", "?"]
        result = queue_act(actions)
        expected = [5, 1]  # Сначала минимум 5, потом 1
        self.assertEqual(result, expected)

    def test_minimum_does_not_update_on_larger_element(self):
        """Тест: минимум не меняется при добавлении большего элемента"""
        actions = ["+ 1", "+ 10", "+ 100", "?"]
        result = queue_act(actions)
        expected = [1]  # Минимум остается 1
        self.assertEqual(result, expected)

    def test_complex_scenario(self):
        """Тест: сложный сценарий"""
        actions = [
            "+ 10", "+ 5", "?",  # [10, 5], мин=5
            "+ 3", "?",  # [10, 5, 3], мин=3
            "-", "?",  # [5, 3], мин=3
            "+ 7", "?",  # [5, 3, 7], мин=3
            "-", "?",  # [3, 7], мин=3
            "+ 2", "?",  # [3, 7, 2], мин=2
            "-", "?"  # [7, 2], мин=2
        ]
        result = queue_act(actions)
        expected = [5, 3, 3, 3, 3, 2, 2]
        self.assertEqual(result, expected)

    def test_only_enqueue_and_query(self):
        """Тест: только добавление и поиск минимума"""
        actions = ["+ 100", "+ 200", "+ 50", "?", "+ 30", "?"]
        result = queue_act(actions)
        expected = [50, 30]
        self.assertEqual(result, expected)

    def test_only_dequeue_after_minimum_removal(self):
        """Тест: удаление после нахождения минимума"""
        actions = ["+ 3", "+ 1", "+ 2", "-", "?"]  # Удаляем 3, минимум 1
        result = queue_act(actions)
        expected = [1]
        self.assertEqual(result, expected)

    def test_single_element(self):
        """Тест: один элемент"""
        actions = ["+ 42", "?", "-"]
        result = queue_act(actions)
        expected = [42]
        self.assertEqual(result, expected)