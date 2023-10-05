--------------------------Задача 1-------------------------------
#Дано число num(значение задаете сами).
#Напечатать “num>0”, если число больше 0, иначе - “num<0”
#
num = int(input("Введите число: "))
if (num > 0):
    print(f"{num} > 0")
if (num == 0):
    print("это ноль, дружище!")
else:
    print(f"{num} < 0")
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите число: -3
# -3 < 0
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите число: 0
# это ноль, дружище!


------------------------Задача 2------------------------------------
#Дано число. Напечатать, если число делится на 3, “ok”, в противном случае - ‘:(’ 
#
num = int(input("Введите число: "))
mod = num % 3
if mod == 0:
    print("Ok!")
else:
    print (":(")
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите число: 21
# Ok!
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите число: 8
# :(


-----------------------------------Задача 3---------------------------------
#пользователь вводит номер месяца (от 1 до 12),
#определить существует ли такой месяц (в печати указать “да” или “нет”)
#
month = int(input("Введите порядковый номер месяца: "))
if month <= 12 and month >= 1:
    print("Такой месяц существует")
else:
    print("Нет такого месяца")
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите порядковый номер месяца: 5
# Такой месяц существует
#
#C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите порядковый номер месяца: 13
# Нет такого месяца
