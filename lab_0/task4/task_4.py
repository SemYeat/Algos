def matr_multipl(a, b):
    c00 = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 10
    c01 = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 10
    c10 = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 10
    c11 = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 10
    return [[c00, c01], [c10, c11]]

def multipl(kef, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n%2 == 0:
        x = multipl(kef, n//2)
        return matr_multipl(x, x)
    else:
        x = multipl(kef, (n-1)//2)
        x2 = matr_multipl(x, x)
        return matr_multipl(x2, kef)

def fib_num(n: int) -> int:
    if n <= 1:
        return n
    matrix = multipl([[0,1], [1, 1]], n)
    return matrix[0][1] % 10

def limits(n: int) -> bool:
    if  0 <= n <= 10**7:
        return True
    else:
        return False

def add_fib_txt():
    with open('input.txt', 'r') as f:
        argum = f.read().strip()
    n = int(argum)
    if limits(n):
        res = str(fib_num(n))
        with open('output.txt', 'w') as f:
            f.write(res)
    else:
        return "Числа выходят за допустимые границы"

if __name__ == '__main__':
    add_fib_txt()