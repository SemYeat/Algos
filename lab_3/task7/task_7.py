import sys
import typing as tp

def read_input() -> tp.Tuple[int, int, int, tp.List[str]]:
    """Чтение входных данных."""
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return 0, 0, 0, []

    n, m, k = map(int, data[0].split())
    # Чтение строк в вертикальном формате
    # Строки записаны в следующих m строках, каждая длиной n
    vertical_lines = data[1:1 + m]
    # Преобразуем вертикальное представление в горизонтальное
    strings = [''] * n
    for i in range(m):
        line = vertical_lines[i]
        for j in range(n):
            if j < len(line):
                strings[j] += line[j]
            else:
                strings[j] += 'a'  # если строка короче n, дополняем 'a'
    return n, m, k, strings

def radix_sort_step(strings: tp.List[tp.Tuple[int, str]], pos: int) -> tp.List[tp.Tuple[int, str]]:
    """Один шаг цифровой сортировки по указанной позиции."""
    # Создаем корзины для букв от 'a' до 'z'
    buckets = [[] for _ in range(26)]
    for idx, s in strings:
        if pos < len(s):
            char_index = ord(s[pos]) - ord('a')
        else:
            char_index = 0  # если строка короче, считаем как 'a'
        buckets[char_index].append((idx, s))
    # Собираем результат
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

def strings_sort(n: int, m: int, k: int, strings: tp.List[str]) -> tp.List[int]:
    """Основная функция сортировки."""
    if n == 0:
        return []

    # Создаем список пар (индекс, строка)
    indexed_strings = [(i + 1, strings[i]) for i in range(n)]
    # Выполняем k фаз цифровой сортировки, начиная с последнего символа
    for phase in range(1, k + 1):
        pos = m - phase  # позиция для сортировки
        indexed_strings = radix_sort_step(indexed_strings, pos)
    # Возвращаем только индексы
    return [idx for idx, _ in indexed_strings]

def main():
    """Главная функция."""
    n, m, k, strings = read_input()
    result = strings_sort(n, m, k, strings)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()