def karl_multiply(A, B):
    n = len(A)
    m = len(B)
    # Базовый случай
    if n == 1 or m == 1:
        result = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                result[i + j] += A[i] * B[j]
        return result
    # Дополняем до одинаковой степени 2^k
    size = max(n, m)
    if size & (size - 1):  # Если не степень двойки
        size = 1
        while size < max(n, m):
            size <<= 1
    A_ext = A + [0] * (size - n)
    B_ext = B + [0] * (size - m)
    # Рекурсивное умножение
    result = karl_recurs(A_ext, B_ext)
    # Убираем лишние нули в конце
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def karl_recurs(A, B):
    n = len(A)
    # Базовый случай
    if n == 1:
        return [A[0] * B[0]]

    mid = n // 2
    # Разделяем многочлены
    a0 = A[:mid]
    a1 = A[mid:]
    b0 = B[:mid]
    b1 = B[mid:]
    # Вычисляем произведения
    p0 = karl_recurs(a0, b0)  # a0 * b0
    p1 = karl_recurs(a1, b1)  # a1 * b1
    # Вычисляем (a0 + a1) * (b0 + b1)
    a_sum = [a0[i] + a1[i] for i in range(mid)]
    b_sum = [b0[i] + b1[i] for i in range(mid)]
    p2 = karl_recurs(a_sum, b_sum)
    # Вычисляем (a0 + a1)(b0 + b1) - p0 - p1 = a0*b1 + a1*b0
    middle = [0] * (2 * n - 1)
    for i in range(len(p2)):
        middle[i] = p2[i]
    for i in range(len(p0)):
        middle[i] -= p0[i]
    for i in range(len(p1)):
        middle[i] -= p1[i]
    # Собираем результат
    result = [0] * (2 * n - 1)
    # p0 (младшие коэффициенты)
    for i in range(len(p0)):
        result[i] += p0[i]
    # middle (средние коэффициенты)
    for i in range(len(middle)):
        result[i + mid] += middle[i]
    # p1 (старшие коэффициенты)
    for i in range(len(p1)):
        result[i + 2 * mid] += p1[i]
    return result

def multiply_simple(A, B):
    """Простое умножение многочленов для проверки"""
    n = len(A)
    m = len(B)
    result = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            result[i + j] += A[i] * B[j]
    return result

def limit(n: int, A: list[int], B: list[int]) -> bool:
    """Проверка ограничений входных данных"""
    if len(A) == n and len(B) == n:
        return True
    return False


def polynomial_multiply_txt():
    """Чтение входных данных и запись результата"""
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    n = int(lines[0])
    A = list(map(int, lines[1].split()))
    B = list(map(int, lines[2].split()))
    if limit(n, A, B):
        # Можно использовать любой метод:
        # result = multiply_simple(A, B)  # Простое умножение для проверки
        result = karl_multiply(A, B)  # Алгоритм Карацубы
        with open('output.txt', 'w') as f:
            f.write(' '.join(map(str, result)))
    else:
        print("Данные выходят за допустимые границы")

def test_example():
    """Тестовый пример из задания"""
    A = [3, 2, 5]  # 3x² + 2x + 5
    B = [5, 1, 2]  # 5x² + x + 2
    result = karl_multiply(A, B)
    expected = [15, 13, 33, 9, 10]  # 15x⁴ + 13x³ + 33x² + 9x + 10
    print(f"Тест: A={A}, B={B}")
    print(f"Результат: {result}")
    print(f"Ожидалось: {expected}")
    print(f"Правильно: {result == expected}")
    return result == expected


if __name__ == "__main__":
    polynomial_multiply_txt()