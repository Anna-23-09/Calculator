import logger as log

def menu_check(val: str) -> str:
    if val.isdigit():
        if len(val) > 1:
            return ' '
        return val
    return ' '

def digit_check(a):
    while not float_check(a):
        print("упс это не число")
        a = input(f"Введите число: ")
        log.write_log(f"число не прошло проверку введено новое {a}, ")
    return float(a)

def float_check(s):
    try:
        float(s)
        return True
    except ValueError:
        return False