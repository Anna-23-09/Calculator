from cheks import menu_check


def menu_inp(val: str) -> int:
    # ars#  что принимает эта функция, стороку ? чтодолжно прийти?
    # den# да она принимает строку, права в контроллре не совсем правильные цифры
    # в интерфейсе можнов коментах посмотреть правильные
    """ Меню верхнего уровня """
    res = ' '
    while res not in val:                           # Сравниваем со строкой которая пришла в вызове
        # Причем тут проверка (menu_check) уже вроде как уже не нужна
        res = menu_check(input('Введите выбор:'))
    else:
        return int(res)


def real_inp(val: int) -> list:          # Возвращаем list из val чисел реальных
    # check ??
    inp: list = []
    for i in range(val):
        print(f'Вам надо ввести {val} реальных(-ое) чисел(-ло):')
        temp1_comp = float(
            input("Введите первое число: "))
        temp2_comp = float(
            input("Введите  числа: "))
        inp.append(complex(temp1_comp, temp2_comp))
    return inp


def complex_inp(val: int) -> list:      # Возвращаем list из val чисел комплексных
    # check ??
    inp: list = []
    for i in range(val):
        print(f'Вам надо ввести {val} комплексных(-ое) чисел(-ло):')
        temp1_comp = float(
            input("Введите действительную часть комплексного числа: "))
        temp2_comp = float(
            input("Введите мнимую часть комплексного числа: "))
        inp.append(complex(temp1_comp, temp2_comp))
    return inp
