
from user_interface import *
from calc_input import menu_inp, real_inp, complex_inp
import model_sum as sum
import model_sub as sub
import model_mult as mult
import model_div as div
import model_pow as pow
import model_mod as rem
import model_div_ as div_
import model_sqrt as sqrt



# all_num = "0123456789.,"


def user_num(start: int):  # ars# для понимания
    if start == 1:                      # что запрашиваем используем переменную

        return real_inp()  # цифра берется из выбора первого меню
    else:
        # если 1 то рациональные если 2 то комплексные
        return complex_inp()


def run():
    draw_menu_start()

    in_run = menu_inp('012')                # первое меню

    if in_run == 1:
        draw_menu_real()                    # меню реальных чисел # возможный выбор 012345678
        in_start = menu_inp('012345678')
        operation(in_run, in_start)
    elif in_run == 2:
        draw_menu_complex()                 # меню комплексных чисел # возможный выбор 0123456
        in_start = menu_inp('0123456')
        operation(in_run, in_start)
    else:
        exit()


def operation_2num(tip_num: int, oper, znak):
    num1 = user_num(tip_num)  # запрашиваем 1е число
    num2 = user_num(tip_num)  # запрашиваем 2е число
    result = oper.init(num1, num2)  # фиксируем результат
    # loger(nam1,znak,nam2,result)    #отправляем в логер

    return result
    # return (result)



def operation(tip_num: int, tip_oper: int):
    if tip_oper == 1:  # Отрисовывается результать сложения первого и второго числа для обоих случиев

        draw_result(operation_2num(tip_num, sum, "+"))  # выводим результат

    elif tip_oper == 2:  # Отрисовывается результать вычитания второго из первого числа для обоих случиев
        draw_result(operation_2num(tip_num, sub, "-"))
    elif tip_oper == 3:  # Отрисовывается результать перемножения первого и второго числа для обоих случиев
        draw_result(operation_2num(tip_num, mult, "*"))
    elif tip_oper == 4:  # Отрисовывается результать деления

        draw_result(operation_2num(tip_num, div, "/"))  # модуль деления
    elif tip_oper == 5:
        if tip_num == 1:
            draw_result(operation_2num(tip_num, div_, "//"))  # модуль целочисленного деления #
        else:
            # модуль возведения в степень #
            draw_result(operation_2num(tip_num, pow, "**"))
    elif tip_oper == 6:
        if tip_num == 1:
            # модуль остатка от деления #
            draw_result(operation_2num(tip_num, rem, "%"))
        else:
            draw_result()   # модуль квадратного корня #
    elif tip_oper == 7:
        # модуль возведения в сепень #
        draw_result(operation_2num(tip_num, pow, "**"))
    elif tip_oper == 8:         
        draw_result(operation_1num(tip_num, sqrt, "sqrt"))      # тут требуется одно число !!!! это типа важно
                                                                # модуль квадратного корня #
    elif tip_oper == 0:         # переход в предыдущие меню
        run()
