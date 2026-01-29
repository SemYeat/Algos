class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.size = len(array)
        self.swaps = []

    def build_heap(self):
        """Построение min-heap (итеративная версия)"""
        for i in range(self.size // 2 - 1, -1, -1):
            self.sift_down_iterative(i)
        return self.swaps

    def sift_down_iterative(self, i):
        """Просеивание элемента вниз (итеративная версия)"""
        while True:
            min_index = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < self.size and self.heap[left] < self.heap[min_index]:
                min_index = left

            if right < self.size and self.heap[right] < self.heap[min_index]:
                min_index = right

            if i == min_index:
                break

            self.swaps.append((i, min_index))
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            i = min_index

def limit(n, array):
    """Проверка ограничений"""
    if 1 <= n <= 10 ** 5 and len(array) == n and all(0 <= x <= 10 ** 9 for x in array):
        return True
    return False

def build_heap_txt():
    """Основная функция"""
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')

    n = int(lines[0])
    array = list(map(int, lines[1].split()))

    if limit(n, array):
        # Можно использовать любую версию
        heap = MinHeap(array)  # Рекурсивная
        # heap = MinHeapIterative(array)  # Итеративная
        swaps = heap.build_heap()
        with open('output.txt', 'w') as f:
            f.write(str(len(swaps)) + '\n')
            for i, j in swaps:
                f.write(f"{i} {j}\n")
    else:
        print("Данные выходят за допустимые границы")

if __name__ == "__main__":
    build_heap_txt()