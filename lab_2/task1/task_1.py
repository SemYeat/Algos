def merge_sort(arr: list[int]) -> list[int]:
    """Сортировка слиянием"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    """Слияние двух отсортированных массивов без сигнальных значений"""
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # Добавляем оставшиеся элементы
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def limits(n: int, array: list[int]) -> bool:
    """Проверка ограничений входных данных"""
    if 1 <= n <= 2 * 10 ** 4 and len(array) == n and all(abs(x) <= 10 ** 9 for x in array):
        return True
    return False

def merge_sort_txt():
    """Чтение входных данных и запись результата"""
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    n = int(lines[0])
    array = list(map(int, lines[1].split()))
    if limits(n, array):
        sorted_array = merge_sort(array)
        with open('output.txt', 'w') as f:
            f.write(' '.join(map(str, sorted_array)))
    else:
        print("Данные выходят за допустимые границы")

if __name__ == "__main__":
    merge_sort_txt()