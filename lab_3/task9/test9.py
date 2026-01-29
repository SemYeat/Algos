import unittest
from lab_3.task9.task_9 import *

class TestClosestPair(unittest.TestCase):
    """Тесты для поиска ближайших точек"""

    def setUp(self):
        """Настройка для тестов"""
        self.original_stdin = sys.stdin
        self.original_stdout = sys.stdout

    def tearDown(self):
        """Восстановление стандартных потоков"""
        sys.stdin = self.original_stdin
        sys.stdout = self.original_stdout

    def test_distance(self):
        """Тест: вычисление расстояния между точками"""
        p1 = Point(0, 0)
        p2 = Point(3, 4)

        result = distance(p1, p2)
        expected = 5.0

        self.assertAlmostEqual(result, expected, places=6)

    def test_distance_same_point(self):
        """Тест: расстояние между одинаковыми точками"""
        p1 = Point(5, 5)
        p2 = Point(5, 5)

        result = distance(p1, p2)
        expected = 0.0

        self.assertAlmostEqual(result, expected, places=6)

    def test_distance_negative_coordinates(self):
        """Тест: расстояние с отрицательными координатами"""
        p1 = Point(-1, -1)
        p2 = Point(-4, -5)

        result = distance(p1, p2)
        expected = 5.0  # sqrt((3)^2 + (4)^2) = 5

        self.assertAlmostEqual(result, expected, places=6)

    def test_brute_force_two_points(self):
        """Тест: переборный метод для двух точек"""
        points = [Point(0, 0), Point(3, 4)]

        result = brute_force(points)
        expected = 5.0

        self.assertAlmostEqual(result, expected, places=6)

    def test_brute_force_three_points(self):
        """Тест: переборный метод для трех точек"""
        points = [Point(0, 0), Point(3, 4), Point(0, 5)]

        result = brute_force(points)
        # Расстояния: (0,0)-(3,4)=5, (0,0)-(0,5)=5, (3,4)-(0,5)=√10≈3.162
        expected = math.sqrt(10)  # ≈3.162277

        self.assertAlmostEqual(result, expected, places=6)

    def test_brute_force_identical_points(self):
        """Тест: переборный метод с одинаковыми точками"""
        points = [Point(7, 7), Point(1, 100), Point(4, 8), Point(7, 7)]

        result = brute_force(points)
        expected = 0.0  # Две одинаковые точки (7,7)

        self.assertAlmostEqual(result, expected, places=6)

    def test_strip_closest(self):
        """Тест: поиск в полосе"""
        strip = [Point(0, 0), Point(1, 1), Point(2, 3), Point(3, 5)]
        d = 5.0

        result = strip_closest(strip, d)
        expected = math.sqrt(2)  # Расстояние между (0,0) и (1,1)

        self.assertAlmostEqual(result, expected, places=6)

    def test_strip_closest_no_closer(self):
        """Тест: поиск в полосе, когда нет точек ближе d"""
        strip = [Point(0, 0), Point(10, 10), Point(20, 20)]
        d = 1.0

        result = strip_closest(strip, d)
        expected = 1.0  # d не изменится

        self.assertAlmostEqual(result, expected, places=6)

    def test_closest_util_small(self):
        """Тест: рекурсивная функция для малого набора"""
        points = [Point(0, 0), Point(3, 4)]
        points_x = sorted(points, key=lambda p: p.x)

        result = closest_util(points_x)
        expected = 5.0

        self.assertAlmostEqual(result, expected, places=6)

    def test_closest_pair_example1(self):
        """Тест: пример 1 из задания (2 точки)"""
        points = [Point(0, 0), Point(3, 4)]

        result = closest_pair(points)
        expected = 5.0

        self.assertAlmostEqual(result, expected, places=4)

    def test_closest_pair_example2(self):
        """Тест: пример 2 из задания (4 точки с одинаковыми)"""
        points = [Point(7, 7), Point(1, 100), Point(4, 8), Point(7, 7)]

        result = closest_pair(points)
        expected = 0.0

        self.assertAlmostEqual(result, expected, places=4)

    def test_closest_pair_example3(self):
        """Тест: пример 3 из задания (11 точек)"""
        points = [
            Point(4, 4), Point(-2, -2), Point(-3, -4), Point(-1, 3),
            Point(2, 3), Point(-4, 0), Point(1, 1), Point(-1, -1),
            Point(3, -1), Point(-4, 2), Point(-2, 4)
        ]

        result = closest_pair(points)
        expected = math.sqrt(2)  # √2 ≈ 1.414213