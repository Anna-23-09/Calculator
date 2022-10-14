from cheks import menu_check

def menu_inp(val: str) -> int:
    """ Меню верхнего уровня """
    res = ' '
    while res not in val:
        res = menu_check(input('Введите выбор:'))
    else:
        return int(res)

def real_inp(val: str) -> int:
    ### check
    inp = float(input('Введите выбор:'))
    return inp

def complex_inp(val: str) -> int:
    # check
    inp = complex(input('Введите выбор:'))
    return inp