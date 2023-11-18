## -------------------------------задача------------------------------------ ##
# Дан текстовый файл. Написать функцию, которая будет подсчитывать количество чисел в строке,
# которые отделены пробелами. Возвращаемое значение должно быть типа int. 
# Применить эту функцию для файла и найти общее кол-во таких чисел.

with open("exampple.txt", 'r') as f:
    s = f.read()

def check_isdigit(s):
    s = input().split()
    nums = list(filter(lambda num: num.isdigit(), s))
    print(int(len(nums)))

# Lorem.txt ipsum32 dolor 56 sit amet 1, consec12tetur adipiscing 4 elit. Aenean 25 ultrices.
# 3