import unittest
from lab_6.task1.task_1 import *

class TestHashSet(unittest.TestCase):
    """Тесты для класса HashSet"""

    def test_hash_function(self):
        """Тест: хэш-функция"""
        hash_set = HashSet(capacity=100)
        # Хэш должен быть в пределах capacity
        self.assertEqual(hash_set._hash(42), 42)
        self.assertEqual(hash_set._hash(-42), 42)
        self.assertEqual(hash_set._hash(0), 0)
        self.assertEqual(hash_set._hash(150), 50)  # 150 % 100 = 50

    def test_add_key(self):
        """Тест: добавление ключа"""
        hash_set = HashSet(capacity=10)

        hash_set.add(5)
        self.assertEqual(hash_set.size, 1)
        self.assertTrue(hash_set.contains(5))

        hash_set.add(5)  # Добавление того же ключа
        self.assertEqual(hash_set.size, 1)  # Размер не должен измениться

    def test_add_multiple_keys(self):
        """Тест: добавление нескольких ключей"""
        hash_set = HashSet(capacity=10)

        keys = [1, 2, 3, 4, 5]
        for key in keys:
            hash_set.add(key)

        self.assertEqual(hash_set.size, 5)
        for key in keys:
            self.assertTrue(hash_set.contains(key))

    def test_add_with_collision(self):
        """Тест: добавление ключей с коллизией хэша"""
        hash_set = HashSet(capacity=1)  # Все ключи будут в одной ячейке

        hash_set.add(1)
        hash_set.add(2)
        hash_set.add(3)

        self.assertEqual(hash_set.size, 3)
        self.assertTrue(hash_set.contains(1))
        self.assertTrue(hash_set.contains(2))
        self.assertTrue(hash_set.contains(3))

    def test_remove_key(self):
        """Тест: удаление ключа"""
        hash_set = HashSet(capacity=10)

        hash_set.add(5)
        self.assertTrue(hash_set.contains(5))

        hash_set.remove(5)
        self.assertFalse(hash_set.contains(5))
        self.assertEqual(hash_set.size, 0)

    def test_remove_nonexistent_key(self):
        """Тест: удаление несуществующего ключа"""
        hash_set = HashSet(capacity=10)

        hash_set.add(5)
        hash_set.remove(10)  # Удаление несуществующего ключа

        self.assertEqual(hash_set.size, 1)
        self.assertTrue(hash_set.contains(5))

    def test_remove_with_collision(self):
        """Тест: удаление ключа с коллизией"""
        hash_set = HashSet(capacity=1)  # Все ключи в одной ячейке

        hash_set.add(1)
        hash_set.add(2)
        hash_set.add(3)

        hash_set.remove(2)

        self.assertEqual(hash_set.size, 2)
        self.assertTrue(hash_set.contains(1))
        self.assertFalse(hash_set.contains(2))
        self.assertTrue(hash_set.contains(3))

    def test_contains(self):
        """Тест: проверка наличия ключа"""
        hash_set = HashSet(capacity=10)

        hash_set.add(5)
        hash_set.add(10)

        self.assertTrue(hash_set.contains(5))
        self.assertTrue(hash_set.contains(10))
        self.assertFalse(hash_set.contains(15))

    def test_large_numbers(self):
        """Тест: работа с большими числами"""
        hash_set = HashSet(capacity=1000)

        large_number = 10 ** 18
        hash_set.add(large_number)
        hash_set.add(-large_number)

        self.assertTrue(hash_set.contains(large_number))
        self.assertTrue(hash_set.contains(-large_number))
        self.assertFalse(hash_set.contains(large_number + 1))


class TestProcessOperations(unittest.TestCase):
    """Тесты для обработки операций"""

    def test_process_operations_example(self):
        """Тест: пример из задания"""
        operations = [
            "A 2",
            "A 5",
            "A 3",
            "? 2",
            "? 4",
            "A 2",
            "D 2",
            "? 2"
        ]

        results = process_operations(operations)
        expected = ["Y", "N", "N"]

        self.assertEqual(results, expected)