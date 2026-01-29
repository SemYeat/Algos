import unittest
from lab_4.task4.task_4 import *


class TestCheckBrackets(unittest.TestCase):
    def test_success_simple(self):
        """Тест: простые корректные последовательности"""
        self.assertEqual(check_brackets("[]"), "Success")
        self.assertEqual(check_brackets("()"), "Success")
        self.assertEqual(check_brackets("{}"), "Success")

    def test_success_nested(self):
        """Тест: вложенные корректные последовательности"""
        self.assertEqual(check_brackets("[()]"), "Success")
        self.assertEqual(check_brackets("{[]}"), "Success")
        self.assertEqual(check_brackets("{[()]}"), "Success")
        self.assertEqual(check_brackets("({[]})"), "Success")

    def test_success_mixed_with_text(self):
        """Тест: корректные последовательности с текстом"""
        self.assertEqual(check_brackets("foo(bar);"), "Success")
        self.assertEqual(check_brackets("a = [1, 2, 3];"), "Success")
        self.assertEqual(check_brackets("if (x > 0) { return x; }"), "Success")
        self.assertEqual(check_brackets("int main() { return 0; }"), "Success")

    def test_success_empty_string(self):
        """Тест: пустая строка (только пробелы)"""
        self.assertEqual(check_brackets(""), "Success")
        self.assertEqual(check_brackets("   "), "Success")
        self.assertEqual(check_brackets("\n\t"), "Success")

    def test_success_no_brackets(self):
        """Тест: строка без скобок"""
        self.assertEqual(check_brackets("hello world"), "Success")
        self.assertEqual(check_brackets("abc123"), "Success")
        self.assertEqual(check_brackets("test"), "Success")
        # Другие примеры
        self.assertEqual(check_brackets("]"), "1")  # только закрывающая
        self.assertEqual(check_brackets("()}"), "3")  # лишняя )
        self.assertEqual(check_brackets("{[}]"), "3")  # } вместо ]
        self.assertEqual(check_brackets("({)}"), "3")  # ) вместо }

    def test_wrong_bracket_type(self):
        """Тест: несоответствие типов скобок"""
        self.assertEqual(check_brackets("([)]"), "3")  # ожидалась ], но пришла )
        self.assertEqual(check_brackets("{[}]"), "3")  # ожидалась ], но пришла }
        self.assertEqual(check_brackets("(]"), "2")  # ожидалась ), но пришла ]
        self.assertEqual(check_brackets("{)"), "2")  # ожидалась }, но пришла )

    def test_unmatched_opening_bracket(self):
        """Тест: непарная открывающая скобка (вторичная ошибка)"""
        # Пример из задания: ((()) -> индекс первой не закрытой скобки
        self.assertEqual(check_brackets("((())"), "1")

        # Другие примеры
        self.assertEqual(check_brackets("("), "1")
        self.assertEqual(check_brackets("[()"), "1")  # первая [ не закрыта
        self.assertEqual(check_brackets("({}"), "1")  # первая ( не закрыта
        self.assertEqual(check_brackets("{[()]"), "1")  # первая { не закрыта

    def test_complex_unmatched_opening(self):
        """Тест: сложные случаи непарных открывающих скобок"""
        # Возвращается первая не закрытая открывающая скобка
        self.assertEqual(check_brackets("([]"), "1")  # первая ( не закрыта
        self.assertEqual(check_brackets("([)"), "3")  # сначала ошибка закрывающей

        # Много не закрытых скобок
        self.assertEqual(check_brackets("((({[[["), "1")
        self.assertEqual(check_brackets("a(b[c{d"), "2")  # ( с индексом 2

    def test_examples_from_task(self):
        """Тест: все примеры из задания"""
        # Пример 1
        self.assertEqual(check_brackets("[]"), "Success")
        # Пример 2
        self.assertEqual(check_brackets("{[]}()"), "Success")

        # Пример 3
        self.assertEqual(check_brackets("[()]"), "Success")

        # Пример 4: ((()) - первая не закрытая открывающая скобка
        self.assertEqual(check_brackets("((())"), "1")
        # Пример
        self.assertEqual(check_brackets("foo(bar);"), "Success")
