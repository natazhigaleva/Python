#---------------------------Задача 1------------------------------
#Пользователь вводит сумму вклада в банк и годовой процент. 
#Найдите сумму вклада через 5 лет.
#
deposit = float(input("Ввведите сумму вклада: ")) <-- Сумма вклада -->
percent = float(input("Процентная ставка: ")) <-- Процентная ставка -->
deposit_term = int(input("Срок вклада: ")) <-- Срок вклада, лет -->
print(deposit*(1 + 0.1)**5) <-- При выполнении условий без пополнения счета и снятия процентов -->
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Ввведите сумму вклада: 100000
# Процентная ставка: 4.6
# Срок вклада: 5
# 161051.00000000006


#---------------------Задача 2-------------------------------------  
#Дано значение температуры в градусах Цельсия. 
#Вывести температуру  в градусах Фаренгейта.
#
c = float(input("Температура по Цельсию: "))
f = 1.8 * c + 32
print(f"Температура {f} по Фаренгейту ")
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Температура по Цельсию: 36.6
# Температура 97.88000000000001 по Фаренгейту 


#-----------------------Задача 3-----------------------------------
#Из трехзначного числа x вычли его последнюю цифру. 
#Когда результат разделили на 10, а к частному слева приписали последнюю цифру числа x, 
#то получилось число 237. Найти число x.
#
print("Введите конечное трехзначное число: ")
num = int(input()) <-- задаем целочисленный тип введенному числу -->
c = num//100 <-- выделяем цифру, приписанную к частному слева -->
n = (num%100) * 10 + c <-- num%100 - выделяем то число, к которому была приписана цифра слева -->
                    <-- *10 - приводим число к трехзначному формату, +с - добавляет последнюю цифру -->
print(n, "- исходное число")
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите конечное трехзначное число: 
# 237
# 372 - исходное число


#------------------------Задача 4------------------------------------
#Дано трехзначное число. Найти произведение цифр.
#
num = int(input("Введите трехзначное число: "))
digit1 = num // 100
digit2 = (num % 100) // 10
digit3 = num % 10
product_of_digits = digit1 * digit2 * digit3
print(f"Произведение цифр заданного числа {num}: {product_of_digits}")
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите трехзначное число: 237
# Произведение цифр заданного числа 237: 42


#-----------------------Задача 5---------------------------------------
#Поменяйте местами значения двух переменных, не используя дополнительных переменных.
#
a = 9
b = 12
a = a + b
b = a - b
a = a - b
print(a, b)
# C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# 12 9



#----------------------Задача 6------------------------------------------
#Дано произвольное число. Найти произведение уникальных цифр
#
num = int(input("Введите число: "))
digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num % 100) // 10
digit4 = num % 10
lst = [digit1, digit2, digit3, digit4]
lst1 = []
count = 0
for i in lst:
     if i not in lst1:
         lst1.append(i)
 print(lst1, "- уникальные цифры")
 import math
 list1 = (lst1)
 result = math.prod(list1)
 print(result, "- произведение уникальных цифр числа" ,num)
 #
 # C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
# Введите число: 1418
# [1, 4, 8] - уникальные цифры
# 32 - произведение уникальных цифр числа 1418
