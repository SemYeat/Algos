def insertion_sort(array_len: int, not_sorted_array: list[int]) -> list[int]:
    """Сортировка вставкой"""
    array = not_sorted_array.copy()
    for i in range(1, array_len):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key
    return array

def limit(array_len: int, array: list[int]) -> bool:
    """Проверка ограничений входных данных"""
    if 1 <= array_len <= 10 ** 3 and all(abs(el) <= 10 ** 9 for el in array):
        return True
    else:
        return False

def add_sort_txt():
    """Чтение входных данных, проверка и запись результата"""
    with open('input.txt', 'r') as f:
        arg = f.read().strip().split('\n')

    array_len = int(arg[0])
    array = list(map(int, arg[1].split()))

    if limits(array_len, array):
        result = insertion_sort(array_len, array)
        res_str = ' '.join(map(str, result))
        with open('output.txt', 'w') as f:
            f.write(res_str)
    else:
        print("Данные выходят за допустимые границы")

if __name__ == '__main__':
    add_sort_txt()