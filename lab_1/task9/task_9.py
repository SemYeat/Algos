def binary_add(binary1: str, binary2: str) -> str:
    """Сложение двух двоичных чисел"""
    n = len(binary1)
    # Преобразуем строки в списки цифр
    a = [int(bit) for bit in binary1]
    b = [int(bit) for bit in binary2]
    c = [0] * (n + 1)
    carry = 0  # Перенос
    for i in range(n - 1, -1, -1):
        # Суммируем биты с учетом переноса
        total = a[i] + b[i] + carry
        c[i + 1] = total % 2  # Текущий бит
        carry = total // 2  # Новый перенос
    c[0] = carry  # Самый старший бит
    # Преобразуем обратно в строку и убираем ведущие нули
    result = ''.join(map(str, c))
    # Убираем ведущие нули, но оставляем хотя бы одну цифру
    result = result.lstrip('0') or '0'
    return result

def limit(binary1: str, binary2: str) -> bool:
    """Проверка ограничений входных данных"""
    if not (1 <= len(binary1) <= 10 ** 3):
        return False
    if not (1 <= len(binary2) <= 10 ** 3):
        return False
    if len(binary1) != len(binary2):
        return False
    if not all(bit in '01' for bit in binary1):
        return False
    if not all(bit in '01' for bit in binary2):
        return False
    return True

def binary_add_txt():
    """Чтение входных данных и запись результата"""
    with open('input.txt', 'r') as f:
        line = f.read().strip()
        binary1, binary2 = line.split()
    if limits(binary1, binary2):
        result = binary_addition(binary1, binary2)
        with open('output.txt', 'w') as f:
            f.write(result)
    else:
        print("Данные выходят за допустимые границы")

if __name__ == "__main__":
    binary_add_txt()