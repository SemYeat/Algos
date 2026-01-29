class InversionCounter:
    def __init__(self):
        self.count = 0

    def merge_sort_count(self, arr):
        """Сортировка слиянием с подсчетом инверсий"""
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort_count(arr[:mid])
        right = self.merge_sort_count(arr[mid:])
        return self.merge_count(left, right)

    def merge_count(self, left, right):
        """Слияние с подсчетом инверсий"""
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                # Все элементы от left[i] до конца left образуют инверсии с right[j]
                self.count += len(left) - i
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def get_inversion_count(self, arr):
        """Основной метод для получения количества инверсий"""
        self.count = 0  # Сбрасываем счетчик
        self.merge_sort_count(arr)
        return self.count

def limits(n: int, array: list[int]) -> bool:
    """Проверка ограничений входных данных"""
    if 1 <= n <= 10 ** 5 and len(array) == n and all(abs(x) <= 10 ** 9 for x in array):
        return True
    return False

def count_inversions_txt():
    """Чтение входных данных и запись результата"""
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    n = int(lines[0])
    array = list(map(int, lines[1].split()))
    if limits(n, array):
        counter = InversionCounter()
        inversions = counter.get_inversion_count(array)
        with open('output.txt', 'w') as f:
            f.write(str(inversions))
    else:
        print("Данные выходят за допустимые границы")

if __name__ == "__main__":
    count_inversions_txt()