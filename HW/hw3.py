---------------------------------Задача 1----------------------------------
# Дано: температура в цельсиях(число) и давление в паскалях (число).
# Написать замерзнет вода или нет.
# Вода замерзает при выполнения двух условий:
#	1. давление в 10^5 Паскаль
#	2. температура меньше либо равно 0 градусов по цельсию 
#
T = float(input("Показания термометра: ,C"))
P = float(input("Показания барометра: ,Па"))
mod = P * (10**5)
if (T <= 0 and mod >= 100000):
    print("Вода замерзла")
else:
    print("Вода не замерзла")
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Показания термометра: ,C +5
# Показания барометра: ,Па 0.1
# Вода не замерзла
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Показания термометра: ,C -5
# Показания барометра: ,Па 1.0
# Вода замерзла


-------------------------------Задача 2----------------------------------------
# Начальник составляет график смены, кто работает а кто нет, он вправе выбрать кого-то одного из рабочих 
# или сразу двоих, используя два параметра worker1 и worker2.
# В каждый параметр он может написать “работает” или “не работает” (только эти варианты)
# Напишите программу, которая в зависимости от выбора начальника выводит информацию  о количестве работников на смене
#
worker1_status = True | False
worker2_status = False | False
if worker1_status and worker2_status:# True = (worker1_status == True) and (worker2_status == True)
    print("Сегодня трудятся 2 работника")
elif worker1_status or worker1_status:# False = (worker1_status == False) or (worker2_status == False)
    print("Сегодня трудится 1 работник")
else:
    print("Эй, начальник! Сегодня же выходной!")
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Сегодня трудится 1 работник
#
worker1_status = True | False
worker2_status = True | False
if worker1_status and worker2_status:# True = (worker1_status == True) and (worker2_status == True)
    print("Сегодня трудятся 2 работника")
elif worker1_status or worker1_status:# False = (worker1_status == False) or (worker2_status == False)
    print("Сегодня трудится 1 работник")
else:
    print("Эй, начальник! Сегодня же выходной!")
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Сегодня трудятся 2 работника
#
worker1_status = False | False
worker2_status = False | False
if worker1_status and worker2_status:# True = (worker1_status == True) and (worker2_status == True)
    print("Сегодня трудятся 2 работника")
elif worker1_status or worker1_status:# False = (worker1_status == False) or (worker2_status == False)
    print("Сегодня трудится 1 работник")
else:
    print("Эй, начальник! Сегодня же выходной!")
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Эй, начальник! Сегодня же выходной!


--------------------------------------Задача 3--------------------------------------------------------------
# Дано два числа. Найдите наибольшее четное число среди них. Если оно не существует, выведите фразу "not found"
#
num_1 = int(input("Введите число"))
num_2 = int(input("Введите число"))
if num_1 % 2 == 0 and num_2 % 2 == 0:
    if num_1 > num_2:
        print(f"Наибольшее из четных чисел {num_1}")
    if num_1 < num_2:
        print(f"Наибольшее из четных чисел {num_2}")
else:
    print("Not found")
#
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите число 5
# Введите число 6
# Not found
# 
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите число 4
# Введите число 10
# Наибольшее из четных чисел 10