from cheks import menu_check

def menu_inp(val: str):
    res = False
    while not res:
        res = menu_check(input('Введите выбор:'))
    else:
        return int(res)

def real_inp(val: str):
    # check
    inp = float(input('Введите выбор:'))
    return inp

def complex_inp(val: str):
    # check
    inp = complex(input('Введите выбор:'))
    return inp