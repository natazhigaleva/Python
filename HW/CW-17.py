## ---------------------------------задача------------------------------------- ##
# Сделайте функцию, которая параметром будет принимать букву и 
# проверять, это буква кириллицы или латиницы.

import re
letter = input("Введите букву: ")

def check_letter():
    latinic = re.findall(r'[A-Za-z]{1}', letter)
    kirillic = re.findall(r'[А-Яа-яЁё]{1}', letter)
    if letter in latinic:
        print(letter, "-", "это латиница")
    elif letter in kirillic:
        print(letter, "-", "это кириллица")
    else:
        print(letter, "-", "это не буква")
check_letter()

# Введите букву: g
# g - это латиница
#  Введите букву: П
# П - это кириллица
#  Введите букву: 5
# 5 - это не буква


## ---------------------------------задача------------------------------------- ##
# Напишите функцию, которая будет принимать произвольную строку и возвращать 
# номер телефона вида 79370000000, если телефона в строке нет функцию должна вернуть 0.

import re

def phone_number():
    number = input()
    phone = re.search(r'\+{0,}[7937]{4}[0-9]{7}', number)    
    if number == phone:
        return number
    else:
        return "0"
print(phone_number())

# 9370000000
# 0
# > 79370000000
# 79370000000
# > +79370001000
# 79370001000

## ---------------------------------задача------------------------------------- ##
# Напишите функцию, которая будет принимать, числа (могут быть разного кол-во) 
# и находить среднее арифметическое для данного набора.

def average_nums():
    nums = [1, 2, 3, 4, 5]
    sum_nums = 0
    for num in nums:
        sum_nums += num
    avg = sum_nums / len(nums)
    print("Среднее арифметическое: ", a)
average_nums()

# Среднее арифметическое:  3.0