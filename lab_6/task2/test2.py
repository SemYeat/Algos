import unittest
from lab_6.task2.task_2 import *


class TestPhoneBook(unittest.TestCase):
    """Тесты для класса PhoneBook"""

    def test_add_key(self):
        """Тест: добавление контакта"""
        phone_book = PhoneBook([])

        phone_book.add_key(1234567, "Alice")
        # Проверяем, что контакт добавлен
        h = hash(1234567)
        self.assertIn(h, phone_book.book)
        self.assertEqual(phone_book.book[h], "Alice")

    def test_add_key_overwrite(self):
        """Тест: перезапись существующего контакта"""
        phone_book = PhoneBook([])

        phone_book.add_key(1234567, "Alice")
        phone_book.add_key(1234567, "Bob")  # Перезаписываем

        h = hash(1234567)
        self.assertEqual(phone_book.book[h], "Bob")  # Должен быть Bob, не Alice

    def test_add_multiple_keys(self):
        """Тест: добавление нескольких контактов"""
        phone_book = PhoneBook([])

        phone_book.add_key(1111111, "Alice")
        phone_book.add_key(2222222, "Bob")
        phone_book.add_key(3333333, "Charlie")

        self.assertEqual(len(phone_book.book), 3)

        h1, h2, h3 = hash(1111111), hash(2222222), hash(3333333)
        self.assertEqual(phone_book.book[h1], "Alice")
        self.assertEqual(phone_book.book[h2], "Bob")
        self.assertEqual(phone_book.book[h3], "Charlie")

    def test_delete_key_exists(self):
        """Тест: удаление существующего контакта"""
        phone_book = PhoneBook([])

        phone_book.add_key(1234567, "Alice")
        h = hash(1234567)
        self.assertIn(h, phone_book.book)

        phone_book.delete_key(1234567)
        self.assertNotIn(h, phone_book.book)

    def test_delete_key_not_exists(self):
        """Тест: удаление несуществующего контакта"""
        phone_book = PhoneBook([])

        phone_book.add_key(1234567, "Alice")
        h = hash(1234567)

        # Удаляем несуществующий контакт
        phone_book.delete_key(9999999)

        # Существующий контакт должен остаться
        self.assertIn(h, phone_book.book)
        self.assertEqual(phone_book.book[h], "Alice")

    def test_check_key_exists(self):
        """Тест: поиск существующего контакта"""
        phone_book = PhoneBook([])

        phone_book.add_key(1234567, "Alice")
        phone_book.check_key(1234567)

        self.assertEqual(phone_book.answer, ["Alice"])

    def test_check_key_not_exists(self):
        """Тест: поиск несуществующего контакта"""
        phone_book = PhoneBook([])

        phone_book.check_key(9999999)

        self.assertEqual(phone_book.answer, ["not found"])

    def test_check_key_after_delete(self):
        """Тест: поиск после удаления"""
        phone_book = PhoneBook([])

        phone_book.add_key(1234567, "Alice")
        phone_book.delete_key(1234567)
        phone_book.check_key(1234567)

        self.assertEqual(phone_book.answer, ["not found"])

    def test_distribute_example1(self):
        """Тест: пример 1 из задания"""
        actions = [
            "add 911 police",
            "add 76213 Mom",
            "add 17239 Bob",
            "find 76213",
            "find 910",
            "find 911",
            "del 910",
            "del 911",
            "find 911",
            "find 76213",
            "add 76213 daddy",
            "find 76213"
        ]

        phone_book = PhoneBook(actions)
        result = phone_book.distribute()

        expected = ["Mom", "not found", "police", "not found", "Mom", "daddy"]
        self.assertEqual(result, expected)

    def test_distribute_example2(self):
        """Тест: пример 2 из задания"""
        actions = [
            "find 3839442",
            "add 123456 me",
            "add 0 granny",
            "find 0",
            "find 123456",
            "del 0",
            "del 0",
            "find 0"
        ]

        phone_book = PhoneBook(actions)
        result = phone_book.distribute()

        expected = ["not found", "granny", "me", "not found"]
        self.assertEqual(result, expected)