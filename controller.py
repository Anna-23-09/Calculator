
from ast import Mult
from modulefinder import Module
from user_interface import *
from calc_input import menu_inp, real_inp, complex_inp
import model_sum as sum
import model_sub as sub
import model_mult as mult

all_num="0123456789.,"

def user_nam(start: int):               #ars# для понимания 
    if start == 1:                      # что запрашиваем используем переменную
        return real_inp(all_num)        #цифра берется из выбора первого меню
    else: complex_inp(all_num)          # если 1 то рациональные если 2 то комплексные
                                        # можно реализовать в файле calc_input могу отправлять аргументом 1 или 2

def run():
    draw_menu_start()
    in_run = menu_inp('012')                # первое меню
    if in_run == 1:
        draw_menu_real()                    # меню реальных чисел
        in_start = menu_inp('012345678')
        operation(in_run,in_start)    
    elif in_run ==2:
        draw_menu_complex()                 # меню комплексных чисел
        in_start = menu_inp('0123456')
        operation(in_run,in_start)
    else: exit()

def operation_2nam(tip_num:int,oper:Module):
    nam1=user_nam(tip_num)      #запрашиваем 1е число
    nam2=user_nam(tip_num)      #запрашиваем 2е число
    result= oper.init(nam1,nam2)  #фиксируем результат
    loger(nam1,oper,nam2,result)#отправляем в логер
    return(result)

def operation(tip_num:int,tip_oper:int): 
    if tip_oper == 1: # Отрисовывается результать сложения первого и второго числа для обоих случиев
        draw_result(operation_2nam(tip_num,sum))         #выводим результат
    elif tip_oper == 2:# Отрисовывается результать вычитания второго из первого числа для обоих случиев
        draw_result(operation_2nam(tip_num,sub))
    elif tip_oper == 3:# Отрисовывается результать перемножения первого и второго числа для обоих случиев
        draw_result(operation_2nam(tip_num,mult))
    elif tip_oper == 4:# Отрисовывается результать деления
        draw_result(#   модуль деления   
    elif tip_oper == 5:
        if tip_num == 1:
            draw_result(# модуль целочисленного деления #  
        else: draw_result(# модуль возведения в степень #
    elif tip_oper == 6:
        if tip_num == 1:
            draw_result(# модуль остатка от деления #   
        else: draw_result(# модуль квадратного корня #
    elif tip_oper == 7:
        draw_result(# модуль возведения в сепень #
    elif tip_oper == 8:
        draw_result(# модуль квадратного корня #
    elif tip_oper == 0:# переход в предыдущие меню
        run()
