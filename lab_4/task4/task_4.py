import sys
from typing import List, Tuple, Optional

def check_brackets(s: str) -> str:
    """
    Проверяет корректность скобочной последовательности.
    Возвращает:
    - "Success" если все скобки корректны
    - индекс (начиная с 1) первой ошибки в противном случае
    """
    stack: List[Tuple[str, int]] = []  # (скобка, индекс)
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for i, char in enumerate(s, 1):
        if char in bracket_pairs.values():  # открывающая скобка
            stack.append((char, i))
        elif char in bracket_pairs.keys():  # закрывающая скобка
            if not stack:  # стек пуст - нет соответствующей открывающей
                return str(i)

            last_bracket, last_index = stack.pop()
            if last_bracket != bracket_pairs[char]:  # несоответствие типов скобок
                return str(i)

    if stack:  # остались не закрытые скобки
        # Возвращаем индекс первой открывающей скобки без пары
        _, first_unclosed_index = stack[0]
        return str(first_unclosed_index)

    return "Success"

def limit(s: str) -> bool:
    return 1 <= len(s) <= 10 ** 5

def main() -> None:
    """Главная функция"""
    data = sys.stdin.read().strip()

    if not limit(data):
        return

    res = check_brackets(data)
    print(res)

if __name__ == "__main__":
    main()