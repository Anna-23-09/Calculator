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


def real_inp():
    # check ??
    return float(input(f"Введите реальное число: "))


def complex_inp() -> complex:
    # check ??
    temp1_comp = float(
        input(f"Введите действительную часть комплексного числа: "))
    temp2_comp = float(
        input(f"Введите мнимую часть комплексного числа: "))
    return complex(temp1_comp, temp2_comp)
