## ------------------------------задача------------------------------- ##
# Дана произвольная строка
# Написать регулярное выражение для поиска в строке серии и номера паспорта. 
# Допускается только запись паспорта из предложенных ниже: 
# 00 00 000000
# или 00 00 000 000
# или 00-00-000-000
# или 00-00-000000
# на месте 0 может стоять любая цифра 
# Программа должны вывести кол-во валидных значений и показать их в консоле

import re
test_string = """
Lorem ipsum 12 34 567890 dolor sit 12-34-567-890 amet, consectetur 12 34 567 890 adipiscing elit. 
Sed libero 12-34-567890 arcu, rutrum 12 34 commodo auctor ut, 123456 faucibus eu leo. 
Quisque a.
"""
reg_ex = r"((\d{2}(\ |\-)){2}(\d{3}(\ |\-)\d{3}|\d{6}))"
passport = re.findall(reg_ex, test_string)
print("Найдено",len(passport), "совпадений:")
print(passport)

# Найдено 4 совпадений:
# [('12 34 567890', '34 ', ' ', '567890', ''), 
# ('12-34-567-890', '34-', '-', '567-890', '-'), 
# ('12 34 567 890', '34 ', ' ', '567 890', ' '), 
# ('12-34-567890', '34-', '-', '567890', '')]


## ------------------------------задача------------------------------- ##
# Дана произвольная строка
# написать регулярное выражение для определения номера автомобиля. 
# Допускается только такая запись номера автомобиля А000АА:
# А-любая буква(латиница)
# 0-любая цифра
# Программа должна вывести кол-во валидных значений и показать их в консоле

import re
test_string = """
Lorem ipsum A111BC dolor sit A111БB amet, 
consectetur a123AA adipiscing elit. 
Sed libero a101bc arcu, rutrum аB123C commodo auctor ut, 
AА123B faucibus eu leo. 
Quisque a.
"""
reg_ex = r"[A-Z]{1}\d{3}[A-Z]{2}"
auto = re.findall(reg_ex, test_string)
print("Количество совпадений:", len(auto))
print(auto)

# Количество совпадений: 1
# ['A111BC']


## ------------------------------задача------------------------------- ##
# Написать регулярное выражение для определения валидных логинов. 
# Валидными считаются те логины, которые удовлетворяют следующим условиям:
# ●	содержат минимум 1 букву латинского алфавита и не содержат буквы других алфавитов
# ●	содержат  минимум 2 цифры
# ●	в конце имени обязательно нужно указывать “login”
# примеры валидных значений:
# n12login
# name22login
# 2name2login
# и т.д.
# Программа должна вывести кол-во валидных значений и показать их в консоле

import re
test_string = """
A21login
a12Login
2name32login
Z1login
_d65name_
С48login
name&23login
"""
reg_ex = r"((\d{0,}[A-z]{1,}\d{2,}(login)))"
login = re.findall(reg_ex, test_string)
print("Валидных логинов:", len(login))
print(login)

# Валидных логинов: 2
# [('A21login', 'A21login', 'login'), 
# ('2name32login', '2name32login', 'login')]


## ------------------------------задача------------------------------- ##
# создать функцию для генерации списка случайными числами 

from random import randint

def generate_list():

   randlist = []
   n = int(input("Введите количество чисел списка: "))
   for _ in range(n):
       randlist.append(randint(-100, 100))
   print(randlist)

generate_list()

# Введите количество чисел списка: 15
# [62, -39, 36, 6, 85, -25, -18, -21, -14, 11, 24, 6, -28, -38, -31]

## ------------------------------задача------------------------------- ##
# используя модуль turtle и создав функцию рисования квадрата, решите следующую задачу
# все треугольники одинакового размера. Для треугольника можно использовать функцию из классной работы.

from turtle import *
import time
def goto():
    penup()
    setposition(-50, 0)
    pendown()

def square():
    pensize(2)
    for _ in range(4):
        fd(80)
        lt(90)
    print(square)

def petal():
    for _ in range(1):
        rt(60)
        fd(80)
        lt(120)
        fd(80)
    for _ in range(3):
        rt(30)
        fd(80)
        lt(120)
        fd(80)
    print(petal)

goto(), square(), petal()
exitonclick()

## ----------------------------------- вариант в цвете ----------------------------##

from turtle import *
import time
bgcolor("grey")
def goto():
    penup()
    setposition(-50, 0)
    pendown()

def square():
    pencolor("red")
    pensize(2)
    for _ in range(4):
        fd(80)
        lt(90)
    print(square)

def petal():
    pencolor("yellow")
    for _ in range(1):
        rt(60)
        fd(80)
        lt(120)
        fd(80)
    for _ in range(3):
        rt(30)
        fd(80)
        lt(120)
        fd(80)
    print(petal)

goto(), square(), petal()
exitonclick()
