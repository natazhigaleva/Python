## ------------------------------задача------------------------------- ##
# Творческое задание
# Можно решить задачу как одной функцией, так и двумя и более. 
# Главное, чтобы получился результат как на картинке. Функция должна принимать произвольный размер снежинки, 
# произвольное кол-во сегментов и произвольный цвет

from turtle import *
import time
def goto(x: int, y: int):
    penup()
    setposition(x, y)
    pendown()
    return goto

def snowflake(color: str, ray: int, size: int):
    pencolor(color)
    pensize(4)
    speed(3)
    lt(90)
    for i in range(ray):
        fd(size)
        bk(size / 4)
        lt(40)
        fd(size / 10)
        bk(size / 10)
        rt(80)
        fd(size / 10)
        bk(size / 10)
        lt(40)
        bk(size / 4)
        lt(40)
        fd(size / 5)
        bk(size / 5)
        rt(80)
        fd(size / 5)
        bk(size / 5)
        lt(40)
        bk(size / 2)
        rt(360 / (ray * 2))
        fd(size / 2)
        bk(size / 5)
        lt(40)
        fd(size / 5)
        bk(size / 5)
        rt(80)
        fd(size / 5)
        bk(size / 5)
        lt(40)
        bk((size / 2) - (size / 5))
        rt(360 / (ray * 2))
    print(snowflake)

def snowflake_1(color: str, ray: int, size: int):
    pencolor(color)
    pensize(4)
    speed(3)
    rt(90)
    for i in range(ray):
        fd(size)
        bk((size / 2) - (size / 5))
        lt(40)
        fd(size / 5)
        bk(size / 5)
        rt(80)
        fd(size / 5)
        bk(size / 5)
        lt(40)
        bk((size / 2) - (size / 5))
        lt(40)
        fd(size - ((size / 5) * 3))
        bk(size - ((size / 5) * 3))
        rt(80)
        fd(size - ((size / 5) * 3))
        bk(size - ((size / 5) * 3))
        lt(40)
        bk(size - ((size / 5) * 3))
        rt(360 / ray)
    print(snowflake_1)

def snowflake_2(color: str, ray: int, size: int):
    pensize(4)
    pencolor(color)
    speed(3)
    lt(90)
    for i in range(ray):
        fd(size)
        bk(size / 4)
        lt(40)
        fd(size / 5)
        bk(size / 5)
        rt(80)
        fd(size / 5)
        bk(size / 5)
        lt(40)
        bk(size / 5)
        lt(40)
        fd((size / 2) - (size / 5))
        bk((size / 2) - (size / 5))
        rt(80)
        fd((size / 2) - (size / 5))
        bk((size / 2) - (size / 5))
        lt(40)
        bk(size - ((size / 5) * 3))
        rt(360 / ray)
    print(snowflake_2)


goto(-180, 150)
snowflake("blue", 6, 100)

goto(0, -50)
snowflake_1("violet", 8, 90)

goto(100, 150)
snowflake_2("cyan", 10, 80)
exitonclick()


## ------------------------------задача------------------------------- ##
# Написать функцию num_to_name_week(num_day_week), которая возвращает имя дня недели(строка)
# Пример: 
# num_to_name_week(1) -> ‘Понедельник’

def num_to_name_week(num_day_week):

    match num_day_week:
        case 1:
            print("Понедельник")
        case 2:
            print("Вторник")
        case 3:
            print("Среда")
        case 4:
            print("Четверг")
        case 5:
            print("Пятница")
        case 6:
            print("Суббота")
        case 7:
            print("Воскресенье")
        case _:
            print("None")

num_to_name_week(6)

# Суббота
