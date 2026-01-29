import unittest
from lab_5.task3.task_3 import *


class TestProcessPackets(unittest.TestCase):
    """Тесты для функции process_packets"""

    def test_example1_no_packets(self):
        """Тест: пример 1 - нет пакетов"""
        result = process_packets(1, [])
        expected = []
        self.assertEqual(result, expected)

    def test_example2_single_packet(self):
        """Тест: пример 2 - один пакет"""
        result = process_packets(1, [(0, 0)])
        expected = [0]
        self.assertEqual(result, expected)

    def test_example3_buffer_full(self):
        """Тест: пример 3 - буфер полон"""
        result = process_packets(1, [(0, 1), (0, 1)])
        expected = [0, -1]
        self.assertEqual(result, expected)

    def test_example4_sequential_packets(self):
        """Тест: пример 4 - последовательные пакеты"""
        result = process_packets(1, [(0, 1), (1, 1)])
        expected = [0, 1]
        self.assertEqual(result, expected)

    def test_example5_single_packet_nonzero_duration(self):
        """Тест: пример 5"""
        result = process_packets(1, [(0, 1)])
        expected = [0]
        self.assertEqual(result, expected)

    def test_example6_zero_duration_packet(self):
        """Тест: пример 6 - пакет с нулевой длительностью"""
        result = process_packets(1, [(1, 0)])
        expected = [1]
        self.assertEqual(result, expected)