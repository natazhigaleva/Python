---------------------------Задача 1------------------------------------
# даны 3 числа, распечатать в порядке возрастания
#
a = int(input("Введите число"))
b = int(input("Введите число"))
c = int(input("Введите число"))
list = [a, b, c]
list.sort()
print(list)
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите число 12
# Введите число 23
# Введите число 4
# [4, 12, 23]
#


---------------------------------Задача 2---------------------------------------------
# Пользователь с клавиатуры вводит количество часов.
# Если полученное значение находится в диапазоне от 0 до 5 нужно вывести надпись Доброй ночи!, 
# если в диапазоне от 5 до 12 - С добрым утром!, если в диапазоне от 12 до 17 - Продуктивного дня!, 
# если в диапазоне от 17 до 22 - Приятного вечера!
# если в диапазоне от 22 до 24 - Спокойной ночи! 
#
time = int(input("Введите текущее время ,час "))
if time >= 0 and time <= 4.9:
    print("Доброй ночи!")
if time >= 5 and time <= 11.9:
    print("С добрым утром!")
if time >= 12 and time <= 16.9:
    print("Продуктивного дня!")
if time >= 17 and time <= 21.9:
    print("Приятного вечера!")
if time >= 22 and time <= 23.9:
    print("Спокойной ночи!")
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите текущее время ,час 3
# Доброй ночи!


---------------------------------Задача 3---------------------------------------------
# определить является ли год високосным 
# 
year = int(input("Введите год"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} Вы родились 29 февраля?")
    else:
        print(f"{year} - невисокосный год")
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите год 1975
# 1975 - невисокосный год