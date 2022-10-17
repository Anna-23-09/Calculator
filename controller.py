import model_sum as sum
import model_sub as sub
import model_mult as mult
import model_div as div
import model_pow as pow
import model_remainder as remainder


all_num="0123456789.,"

def user_nam(start: int):
    if start == 1:
        return real_inp(all_num)
    else: complex_inp(all_num)


def run():
    draw_menu_start()
    
    in_run = menu_inp('012')                # первое меню 
    if in_run == 1:
        draw_menu_real()                    # меню реальных чисел # возможный выбор 012345678
        in_start = menu_inp('012345678')
    elif in_run ==2:
        draw_menu_complex()                 # меню комплексных чисел # возможный выбор 0123456
        in_start = menu_inp('012345678')
    else: exit
      
    if in_start == 1:
        draw_result(sum.init(user_nam,user_nam))
    elif in_start == 2:
        draw_result(sub.init(user_nam,user_nam))
    elif in_start == 3:
        draw_result(mult.init(user_nam,user_nam))


run()
