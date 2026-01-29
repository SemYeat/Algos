import unittest
from lab_3.task7.task_7 import *
import io


class TestDigitalSort(unittest.TestCase):
    """Тесты для цифровой сортировки"""

    def setUp(self):
        """Настройка для тестов"""
        self.original_stdin = sys.stdin
        self.original_stdout = sys.stdout

    def tearDown(self):
        """Восстановление стандартных потоков"""
        sys.stdin = self.original_stdin
        sys.stdout = self.original_stdout

    def test_read_input_vertical_format(self):
        """Тест: чтение данных в вертикальном формате"""
        # Входные данные из примечания:
        # bab (индекс 1), bba (индекс 2), baa (индекс 3)
        # В вертикальном формате это:
        # bbb (первые символы: b, b, b)
        # aba (вторые символы: a, b, a)
        # baa (третьи символы: b, a, a)
        input_data = """3 3 1
bbb
aba
baa"""
        sys.stdin = io.StringIO(input_data)

        n, m, k, strings = read_input()

        self.assertEqual(n, 3)
        self.assertEqual(m, 3)
        self.assertEqual(k, 1)
        self.assertEqual(strings, ['bab', 'bba', 'baa'])

    def test_radix_sort_step_single_position(self):
        """Тест: один шаг цифровой сортировки"""
        # Исходные строки: bab (1), bba (2), baa (3)
        strings = [(1, 'bab'), (2, 'bba'), (3, 'baa')]

        # Сортируем по последнему символу (позиция 2)
        # Последние символы: b, a, a
        # Порядок: bba (a), baa (a), bab (b)
        sorted_strings = radix_sort_step(strings, 2)

        expected = [(2, 'bba'), (3, 'baa'), (1, 'bab')]
        self.assertEqual(sorted_strings, expected)

    def test_strings_sort_phase1(self):
        """Тест: 1 фаза сортировки"""
        n, m, k = 3, 3, 1
        strings = ['bab', 'bba', 'baa']  # индексы: 1, 2, 3

        result = strings_sort(n, m, k, strings)

        # После 1 фазы (последний символ):
        # bab (1) - последний b
        # bba (2) - последний a
        # baa (3) - последний a
        # Порядок: сначала строки с a, потом с b
        # Среди строк с a: сохраняется исходный порядок (2, потом 3)
        expected = [2, 3, 1]
        self.assertEqual(result, expected)

    def test_strings_sort_phase2(self):
        """Тест: 2 фазы сортировки"""
        n, m, k = 3, 3, 2
        strings = ['bab', 'bba', 'baa']  # индексы: 1, 2, 3

        result = strings_sort(n, m, k, strings)

        # После 2 фаз (последний и предпоследний символы):
        # Полная сортировка по последним 2 символам
        # bab (1): ab -> второй
        # bba (2): ba -> первый
        # baa (3): aa -> третий
        # Алфавитный порядок последних 2 символов:
        # aa (baa, индекс 3), ab (bab, индекс 1), ba (bba, индекс 2)
        expected = [3, 1, 2]
        self.assertEqual(result, expected)

    def test_strings_sort_phase3(self):
        """Тест: 3 фазы сортировки (полная сортировка)"""
        n, m, k = 3, 3, 3
        strings = ['bab', 'bba', 'baa']  # индексы: 1, 2, 3

        result = strings_sort(n, m, k, strings)

        # Полная сортировка по всем символам:
        # baa (3) - первый
        # bab (1) - второй
        # bba (2) - третий
        expected = [3, 1, 2]
        self.assertEqual(result, expected)

    def test_main_example1(self):
        """Тест: полный пример 1 с main()"""
        # Пример из задания: 3 3 1
        input_data = """3 3 1
bbb
aba
baa"""
        expected_output = "2 3 1\n"

        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()

        main()

        result = sys.stdout.getvalue()
        self.assertEqual(result, expected_output)

    def test_main_example2(self):
        """Тест: полный пример 2 с main()"""
        # Пример из задания: 3 3 2
        input_data = """3 3 2
bbb
aba
baa"""
        expected_output = "3 1 2\n"

        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()

        main()

        result = sys.stdout.getvalue()
        self.assertEqual(result, expected_output)

    def test_main_example3(self):
        """Тест: полный пример 3 с main()"""
        # Пример из задания: 3 3 3
        input_data = """3 3 3
bbb
aba
baa"""
        expected_output = "3 1 2\n"

        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()

        main()

        result = sys.stdout.getvalue()
        self.assertEqual(result, expected_output)