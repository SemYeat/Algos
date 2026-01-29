import unittest
from lab_5.task4.task_4 import *

def is_min_heap(arr):
    """Проверка, является ли массив корректной min-heap"""
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

class TestMinHeap(unittest.TestCase):
    """Тесты для класса MinHeap"""

    def test_example1_from_task(self):
        """Тест: пример 1 из задания"""
        array = [5, 4, 3, 2, 1]
        heap = MinHeap(array.copy())
        swaps = heap.build_heap()

        # Проверяем количество свапов (в примере было 3)
        self.assertLessEqual(len(swaps), 4 * len(array))

        # Проверяем, что полученный массив - корректная min-heap
        self.assertTrue(is_min_heap(heap.heap))

        # Проверяем, что результат - перестановка исходного массива
        expected_heap_sorted = sorted(array)
        self.assertEqual(sorted(heap.heap), expected_heap_sorted)

    def test_example2_from_task(self):
        """Тест: пример 2 из задания (уже min-heap)"""
        array = [1, 2, 3, 4, 5]
        heap = MinHeap(array.copy())
        swaps = heap.build_heap()

        # Должно быть 0 свапов, так как массив уже min-heap
        self.assertEqual(len(swaps), 0)

        # Массив не должен измениться (уже min-heap)
        self.assertEqual(heap.heap, array)
        self.assertTrue(is_min_heap(heap.heap))

    def test_single_element(self):
        """Тест: один элемент"""
        array = [42]
        heap = MinHeap(array.copy())
        swaps = heap.build_heap()

        self.assertEqual(len(swaps), 0)
        self.assertEqual(heap.heap, [42])
        self.assertTrue(is_min_heap(heap.heap))

    def test_two_elements_already_heap(self):
        """Тест: два элемента, уже min-heap"""
        array = [1, 2]
        heap = MinHeap(array.copy())
        swaps = heap.build_heap()

        self.assertEqual(len(swaps), 0)
        self.assertEqual(heap.heap, [1, 2])
        self.assertTrue(is_min_heap(heap.heap))

    def test_two_elements_need_swap(self):
        """Тест: два элемента, нужен swap"""
        array = [2, 1]
        heap = MinHeap(array.copy())
        swaps = heap.build_heap()

        # Должен быть 1 swap
        self.assertEqual(len(swaps), 1)
        self.assertEqual(heap.heap, [1, 2])
        self.assertTrue(is_min_heap(heap.heap))

    def test_three_elements(self):
        """Тест: три элемента"""
        array = [3, 1, 2]
        heap = MinHeap(array.copy())
        swaps = heap.build_heap()

        self.assertLessEqual(len(swaps), 4 * len(array))
        self.assertTrue(is_min_heap(heap.heap))

        # Проверяем, что результат - перестановка исходного массива
        self.assertEqual(sorted(heap.heap), sorted(array))

    def test_reverse_sorted(self):
        """Тест: обратно отсортированный массив"""
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        heap = MinHeap(array.copy())
        swaps = heap.build_heap()

        self.assertLessEqual(len(swaps), 4 * len(array))
        self.assertTrue(is_min_heap(heap.heap))

        # Минимальный элемент должен быть в корне
        self.assertEqual(heap.heap[0], 1)

    def test_random_array(self):
        """Тест: случайный массив"""
        array = [9, 3, 7, 1, 5, 8, 2, 6, 4]
        heap = MinHeap(array.copy())
        swaps = heap.build_heap()

        self.assertLessEqual(len(swaps), 4 * len(array))
        self.assertTrue(is_min_heap(heap.heap))

        # Проверяем, что все элементы сохранены
        self.assertEqual(sorted(heap.heap), sorted(array))