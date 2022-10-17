# Calculator status WiP
| person              | to do               |   status |   done   |  есть изменения для внесения     |
|---|---|---|---|---|
| Анна Толстова       | complex.py          |   | X |   |
| Арсений Беляев aza  | conroller.py        |   |   |   |
| Ирина Боярчукова    |                     |   |   |   |
| Анна Орлова         |                     |   |   |   |
| Вадим Борзиков      |                     |   |   |   |
| Денис aka Goofy     | user_interface.py   |   | X |   |
## main.py
    calls controller (.py)
нашел пустую строчку чтобы залетело без проблем
# нужны добровольци на разработку модулей математических оперкаций, звучит страшно но не очень) надо создать фаил и описать в нем метод который принимает 1 или 2 числа и производит математическую операцию с ним и возвращает результат. все готово)))
## controller.
    num1: float
    num2: float

    com1: Complex(n1, n2)
    com2: Complex(n3, n4)
    1. call user_interface

## user_interface.py    view —> меню работы с Юзером
    draw_start_menu()
    draw_real_menu()
    draw_complex_menu()

    start >
    1. Real
        calls contoller(1)
    2. Complex
        calls contoller(2)
    0. exit
        calls contoller(0)

    Real >
    1. + sum
    2. - minus
    3. * multiply
    4. division
        1. / division
        2. // division
        3. % division
    4. ** power
    5. sqrt

    9. change numbers
    0. previous menu 

    Complex >
    1. sum
    2. minus
    3. multiply
    4. division
    5. power
    6. sqrt

## except.py —> Обработка исключений

## input.py
    1. input_complex.py
    2. input_real.py

## real_num.py

    1. + sum
        * > import calc_sum
        * > call calc_sum(n1, n2)
        * > return res_num
    2. - minus
        * > import calc_minus
        * >> call calc_minus(n1, n2)
        * > return res_num
    3. * multiply
        * > import calc_mult
        * >> call calc_mult(n1, n2)
        * > return res_num
    4. / division
            * > import calc_div
            * > op = /
            * >> call calc_div(op, n1, n2)
            * > return res_num
    5. // division
            * > import calc_div
            * > op = //
            * >> call calc_div(op, n1, n2)
            * > return res_num
    6. % division
            * > import calc_div
            * > op = %
            * >> call calc_div(op, n1, n2)
            * > return res_num
    7. ** power
    8. sqrt

    0. previous menu

## complex.py —> Работа с Комплексными числами

    1. sum
    2. minus
    3. multiply
    4. division
    5. power
    6. sqrt

    0. previous menu
