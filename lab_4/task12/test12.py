import unittest
from lab_4.task12.task_12 import *


class TestFormationCommands(unittest.TestCase):
    """Тесты для функции formation_commands"""

    def test_example1(self):
        """Тест: пример 1 из задания"""
        n, m = 3, 3
        commands = ["left 2 1", "right 3 1", "name 1"]
        result = formation_commands(n, m, commands)
        expected = ["2 3"]
        self.assertEqual(result, expected)

    def test_example2(self):
        """Тест: пример 2 из задания"""
        n, m = 3, 4
        commands = ["left 2 1", "right 3 1", "leave 1", "name 2"]
        result = formation_commands(n, m, commands)
        expected = ["0 3"]
        self.assertEqual(result, expected)

    def test_single_soldier(self):
        """Тест: один солдат в строю"""
        n, m = 1, 1
        commands = ["name 1"]
        result = formation_commands(n, m, commands)
        expected = ["0 0"]
        self.assertEqual(result, expected)

    def test_left_command(self):
        """Тест: команда left"""
        n, m = 3, 2
        commands = ["left 2 1", "name 1"]
        result = formation_commands(n, m, commands)
        expected = ["2 0"]
        self.assertEqual(result, expected)

    def test_right_command(self):
        """Тест: команда right"""
        n, m = 3, 2
        commands = ["right 2 1", "name 1"]
        result = formation_commands(n, m, commands)
        expected = ["0 2"]
        self.assertEqual(result, expected)

    def test_leave_command(self):
        """Тест: команда leave"""
        n, m = 3, 3
        commands = ["right 2 1", "leave 1", "name 2"]
        result = formation_commands(n, m, commands)
        expected = ["0 0"]  # Солдат 2 остался один
        self.assertEqual(result, expected)

    def test_mixed_left_right_commands(self):
        """Тест: смешанные команды left и right"""
        n, m = 5, 5
        commands = ["right 2 1", "left 3 1", "right 4 2", "left 5 3", "name 1"]
        # Строй: 5 3 1 2 4
        result = formation_commands(n, m, commands)
        expected = ["3 2"]  # Соседи солдата 1: слева 3, справа 2
        self.assertEqual(result, expected)

    def test_leave_and_rejoin(self):
        """Тест: уход и возвращение в строй"""
        n, m = 3, 7
        commands = ["right 2 1", "right 3 2", "name 2",  # 1 2 3
                    "leave 2", "name 1", "name 3",  # 1 3
                    "left 2 1", "name 1"]  # 2 1 3
        result = formation_commands(n, m, commands)
        expected = ["1 3", "0 3", "1 0", "2 3"]
        self.assertEqual(result, expected)
