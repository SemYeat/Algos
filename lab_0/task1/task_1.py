

def add(a: int,b: int) -> int:
    return a+b

def limits(a: int, b: int) -> bool:
    if abs(a) <= 10**9 and abs(b) <= 10**9:
        return True
    else:
        return False

def add_txt():
    with open('input.txt', 'r') as f:
        argum = f.readlines()
    a, b = map(int, argum[0].split(' '))
    if limits(a, b):
        res = str(add(a, b))
        with open('output.txt', 'w') as f:
            f.write(res)
    else:
        return "Числа выходят за допустимые границы"

if __name__ == '__main__':
    add_txt()



