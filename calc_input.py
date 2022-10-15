from cheks import menu_check

def menu_inp(val: str) -> int:   #ars#  что принимает эта функция, стороку ? чтодолжно прийти?
                                     #den# да она принимает строку, права в контроллре не совсем правильные цифры
                                     # в интерфейсе можнов коментах посмотреть правильные
   
    """ Меню верхнего уровня """
    res = ' '
    while res not in val:
        res = menu_check(input('Введите выбор:'))   # Причем тут проверка (menu_check) уже вроде как уже не нужна
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