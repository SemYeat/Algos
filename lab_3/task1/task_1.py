from utils import File
from random import randint

def quick_sort(l: list[int]) -> list[int]:
    x = l.copy()
    if len(x) > 1:
        pivot = x[randint(0, len(x) - 1)]
        start = [i for i in x if i < pivot]
        equal = [i for i in x if i == pivot]
        end = [i for i in x if i > pivot]
        x = quick_sort(start) + equal + quick_sort(end)
    return x

def limit(n: int, l: list[int]) -> bool:
    if 1 <= n <= 10**4 and len(l) == n and all(abs(x) <= 10**9 for x in l):
        return True
    else:
        return False

def quick_sort_txt():
    f = File(__file__)
    arguments = f.read()
    a = int(arguments[0])
    b = list(map(int, arguments[1].split(" ")))

    if limit(a, b):
        res = " ".join(map(str, quick_sort(b)))
        f.write(res)

if __name__ == "__main__":
    quick_sort_txt()