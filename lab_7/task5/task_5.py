def lcs(arr1, arr2, arr3):
    """Оптимизированная версия с меньшим использованием памяти"""
    n, m, l = len(arr1), len(arr2), len(arr3)

    # Используем только два слоя вместо всей 3D матрицы
    dp = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(2)]
    for i in range(1, n + 1):
        curr = i % 2
        prev = 1 - curr

        for j in range(1, m + 1):
            for k in range(1, l + 1):
                dp[curr][j][k] = max(dp[prev][j][k], dp[curr][j - 1][k], dp[curr][j][k - 1])

                if arr1[i - 1] == arr2[j - 1] == arr3[k - 1]:
                    dp[curr][j][k] = max(dp[curr][j][k], dp[prev][j - 1][k - 1] + 1)
    return dp[n % 2][m][l]

def limit(n, arr_a, m, arr_b, l, arr_c):
    """Проверка ограничений входных данных"""
    if 1 <= n <= 100 and len(arr_a) == n and all(abs(x) < 10 ** 9 for x in arr_a):
        if 1 <= m <= 100 and len(arr_b) == m and all(abs(x) < 10 ** 9 for x in arr_b):
            if 1 <= l <= 100 and len(arr_c) == l and all(abs(x) < 10 ** 9 for x in arr_c):
                return True
    return False


def lcs_txt():
    """Чтение входных данных и запись результата"""
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')

    n = int(lines[0])
    arr_a = list(map(int, lines[1].split()))

    m = int(lines[2])
    arr_b = list(map(int, lines[3].split()))

    l = int(lines[4])
    arr_c = list(map(int, lines[5].split()))

    if limit(n, arr_a, m, arr_b, l, arr_c):
        result = lcs(arr_a, arr_b, arr_c)
        with open('output.txt', 'w') as f:
            f.write(str(result))
    else:
        print("Данные выходят за допустимые границы")

if __name__ == "__main__":
    lcs_txt()