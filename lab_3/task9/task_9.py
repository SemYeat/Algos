import sys
import math
from typing import List, Tuple

class Point:
    """Класс для представления точки"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def distance(p1: Point, p2: Point) -> float:
    """Вычисление евклидова расстояния между двумя точками"""
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def brute_force(points: List[Point]) -> float:
    """Переборный метод для нахождения минимального расстояния (для небольших наборов)"""
    n = len(points)
    min_dist = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def strip_closest(strip: List[Point], d: float) -> float:
    """Нахождение ближайших точек в полосе шириной d"""
    min_dist = d
    n = len(strip)
    # Сортируем точки по y-координате
    strip.sort(key=lambda p: p.y)
    # Для каждой точки проверяем только следующие 7 точек
    for i in range(n):
        j = i + 1
        while j < n and (strip[j].y - strip[i].y) < min_dist:
            min_dist = min(min_dist, distance(strip[i], strip[j]))
            j += 1
    return min_dist

def closest_util(points_x: List[Point]) -> float:
    """Рекурсивная функция для нахождения минимального расстояния"""
    n = len(points_x)
    # Если точек мало, используем перебор
    if n <= 3:
        return brute_force(points_x)

    # Находим среднюю точку
    mid = n // 2
    mid_point = points_x[mid]
    # Рекурсивно находим минимальные расстояния в левой и правой половинах
    dl = closest_util(points_x[:mid])
    dr = closest_util(points_x[mid:])
    # Минимальное из двух расстояний
    d = min(dl, dr)
    # Создаем полосу из точек, которые находятся на расстоянии меньше d от средней линии
    strip = []
    for point in points_x:
        if abs(point.x - mid_point.x) < d:
            strip.append(point)
    # Находим минимальное расстояние в полосе
    return min(d, strip_closest(strip, d))

def closest_pair(points: List[Point]) -> float:
    """Основная функция для нахождения минимального расстояния между точками"""
    if len(points) < 2:
        return 0.0

    # Сортируем точки по x-координате
    points_x = sorted(points, key=lambda p: p.x)
    return closest_util(points_x)

def read_input() -> Tuple[int, List[Point]]:
    """Чтение входных данных"""
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return 0, []

    n = int(data[0])
    points = []
    for i in range(1, n + 1):
        if i < len(data):
            x, y = map(int, data[i].split())
            points.append(Point(x, y))
    return n, points

def validate_input(n: int, points: List[Point]) -> bool:
    """Проверка корректности входных данных"""
    if not (1 <= n <= 10 ** 5):
        return False

    if len(points) != n:
        return False

    for point in points:
        if not (-10 ** 9 <= point.x <= 10 ** 9 and -10 ** 9 <= point.y <= 10 ** 9):
            return False

    return True

def main():
    """Главная функция"""
    n, points = read_input()
    if not validate_input(n, points):
        return

    if n < 2:
        print("0.0000")
        return

    # Находим минимальное расстояние
    min_distance = closest_pair(points)

    # Выводим результат с 4 знаками после запятой
    print(f"{min_distance:.4f}")

if __name__ == "__main__":
    main()