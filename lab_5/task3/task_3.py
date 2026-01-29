def process_packets(buffer_size: int, packages: list) -> list:
    """Обработка сетевых пакетов (исправленная версия)"""
    if not packages:
        return []
    result = []
    finish_times = []  # Время окончания обработки пакетов в буфере
    current_time = 0
    for arrival, duration in packages:
        # Удаляем обработанные пакеты из буфера
        while finish_times and finish_times[0] <= arrival:
            finish_times.pop(0)
        if len(finish_times) < buffer_size:
            # Время начала обработки
            if not finish_times:
                start_time = arrival  # Буфер пуст
            else:
                start_time = max(arrival, finish_times[-1])
            result.append(start_time)
            # Добавляем время окончания обработки
            finish_time = start_time + duration
            finish_times.append(finish_time)
        else:
            # Буфер полон
            result.append(-1)
    return result

def limit(buffer_size: int, package_count: int, packages: list) -> bool:
    """Проверка ограничений"""
    if 1 <= buffer_size <= 10 ** 5 and 1 <= package_count <= 10 ** 5:
        if len(packages) == package_count:
            for a, p in packages:
                if not (0 <= a <= 10 ** 6 and 0 <= p <= 10 ** 3):
                    return False
            return True
    return False

def process_packets_txt():
    """Основная функция"""
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        return

    buffer_size, package_count = map(int, lines[0].split())
    packages = []
    for i in range(1, min(package_count + 1, len(lines))):
        a, p = map(int, lines[i].split())
        packages.append((a, p))

    if limit(buffer_size, package_count, packages):
        result = process_packets(buffer_size, packages)
        with open('output.txt', 'w') as f:
            f.write('\n'.join(map(str, result)))
    else:
        print("Ошибка в данных")

if __name__ == "__main__":
    process_packets_txt()