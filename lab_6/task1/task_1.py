import sys
from typing import List, Optional

class Node:
    """Узел связного списка для разрешения коллизий"""
    def __init__(self, key: int, value: bool = True):
        self.key = key
        self.value = value
        self.next: Optional['Node'] = None

class HashSet:
    """Реализация множества с помощью хэш-таблицы"""
    def __init__(self, capacity: int = 100000):
        self.capacity = capacity
        self.size = 0
        self.table: List[Optional[Node]] = [None] * capacity

    def _hash(self, key: int) -> int:
        """Хэш-функция для целых чисел"""
        # Простая хэш-функция с учетом знака числа
        return abs(key) % self.capacity

    def add(self, key: int) -> None:
        """Добавление ключа в множество"""
        index = self._hash(key)
        # Проверяем, есть ли уже такой ключ
        current = self.table[index]
        while current:
            if current.key == key:
                return  # Ключ уже существует
            current = current.next
        # Добавляем новый узел в начало цепочки
        new_node = Node(key)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1

    def remove(self, key: int) -> None:
        """Удаление ключа из множества"""
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def contains(self, key: int) -> bool:
        """Проверка наличия ключа в множестве"""
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

def process_operations(operations: List[str]) -> List[str]:
    """Обработка списка операций над множеством"""
    hash_set = HashSet()
    results = []
    for op in operations:
        if not op.strip():
            continue

        parts = op.strip().split()
        if len(parts) != 2:
            continue

        command, value_str = parts
        try:

            value = int(value_str)
        except ValueError:
            continue

        if command == 'A':
            hash_set.add(value)
        elif command == 'D':
            hash_set.remove(value)
        elif command == '?':
            if hash_set.contains(value):
                results.append('Y')
            else:
                results.append('N')
    return results

def read_input() -> List[str]:
    """Чтение входных данных"""
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return []

    # Первая строка - количество операций
    try:
        n = int(data[0])
    except ValueError:
        return []

    # Возвращаем только операции
    return data[1:1 + n] if len(data) > 1 else []

def validate_input(operations: List[str]) -> bool:
    """Проверка корректности входных данных"""
    if not operations:
        return False

    # Проверяем каждую операцию
    for op in operations:
        parts = op.strip().split()
        if len(parts) != 2:
            return False

        command, value_str = parts
        if command not in ('A', 'D', '?'):
            return False

        try:
            value = int(value_str)
            if abs(value) > 10 ** 18:
                return False
        except ValueError:
            return False

    return True

def main():
    """Главная функция"""
    operations = read_input()
    if not validate_input(operations):
        return

    results = process_operations(operations)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()