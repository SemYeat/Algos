import math
import typing as tp
from utils import File


def perfect_sq(a):
    b = int(math.isqrt(a))
    return b * b == a

def fib(n: int) -> str:
    if perfect_sq(5 * n * n + 4) or perfect_sq(5 * n * n - 4):
        return "Yes"
    else:
        return "No"

def limit(length: int, num: tp.List[int]) -> bool:
    if 1 <= length == len(num) <= 10 ** 6 and all(1 <= x <= 10 ** 5000 - 1 for x in num):
        return True
    else:
        return False

def fib_txt():
    f = File(__file__)
    arguments = f.read()
    length = int(arguments[0])
    numbers = [int(arguments[i]) for i in range(1, length + 1)]
    if limit(length, numbers):
        res = "\n".join(fib(n) for n in numbers)
        f.write(res)

if __name__ == "__main__":
    fib_txt()