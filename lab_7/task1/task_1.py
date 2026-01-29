def exchange(money: int, coins: list[int]) -> int:
    """Минимальное количество монет для размена (неограниченное количество монет)"""
    INF = float('inf')
    dp = [INF] * (money + 1)
    dp[0] = 0

    for i in range(1, money + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money] if dp[money] != INF else -1

def exchange_limited(money: int, coins: list[int], counts: list[int]) -> int:
    """Минимальное количество монет для размена (ограниченное количество монет)"""
    INF = float('inf')
    dp = [INF] * (money + 1)
    dp[0] = 0

    for coin, count in zip(coins, counts):
        # Обработка ограниченного количества монет
        for _ in range(count):
            for j in range(money, coin - 1, -1):
                if dp[j - coin] != INF:
                    dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[money] if dp[money] != INF else -1


def limits(money: int, k: int, coins: list[int]) -> bool:
    """Проверка ограничений входных данных"""
    if not (1 <= money <= 10 ** 3):
        return False
    if not (1 <= k <= 100):
        return False
    if len(coins) != k:
        return False
    if not all(1 <= coin <= 10 ** 3 for coin in coins):
        return False
    return True


def exchange_txt():
    """Чтение входных данных и запись результата"""
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')

    # Вариация 1: только монеты (без ограничений)
    if len(lines) == 2:
        money, k = map(int, lines[0].split())
        coins = list(map(int, lines[1].split()))

        if limits(money, k, coins):
            result = exchange(money, coins)
            with open('output.txt', 'w') as f:
                f.write(str(result))
        else:
            print("Данные выходят за допустимые границы")

    # Вариация 2: с ограничениями количества монет
    elif len(lines) == 3:
        money, k = map(int, lines[0].split())
        coins = list(map(int, lines[1].split()))
        counts = list(map(int, lines[2].split()))

        if limits(money, k, coins) and len(counts) == k and all(c >= 0 for c in counts):
            result = exchange_limited(money, coins, counts)
            with open('output.txt', 'w') as f:
                f.write(str(result))
        else:
            print("Данные выходят за допустимые границы")


if __name__ == "__main__":
    exchange_txt()