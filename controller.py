
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
    elif in_run ==2:
        draw_menu_complex()                 # меню комплексных чисел
        in_start = menu_inp('012345678')
    else: exit
      
    if in_start == 1: # Отрисовывается результать сложения первого и второго числа для обоих случиев
        draw_result(sum.init(user_nam(in_run),user_nam(in_run)))
    elif in_start == 2:# Отрисовывается результать вычитания второго из первого числа для обоих случиев
        draw_result(sub.init(user_nam(in_run),user_nam(in_run)))
    elif in_start == 3:# Отрисовывается результать перемножения первого и второго числа для обоих случиев
        draw_result(mult.init(user_nam(in_run),user_nam(in_run)))


run()