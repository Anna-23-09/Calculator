
from numbers import Complex
from cheks import menu_check

def menu_inp(val: str):
    res = False
    while not res:
        res = menu_check(input('Введите выбор:'))
    else:
        return int(res)

def real_inp():
    # check
    inp = float(input('Введите выбор:'))
    return inp

def complex_inp():
    # check
    inp = Complex(input('Введите выбор:'))
    return inp

print(menu_inp())
