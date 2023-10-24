#------------------------------задача----------------------------------#

## Найдите количество различных элементов данного массива.

my_list = ['1', '13', 'dfg']
new_list = ()
counter = 0
for element in range(len(my_list)):
    my_list[element] = str(my_list[element])
    if my_list[element] not in new_list:
        counter += 1
print(counter)

#------------------------------задача----------------------------------#

## В данном массиве найти два наименьших элемента.

from random import randint
a = []         
for i in range (10):    
    a.append (randint (1, 100)) 
print (a)
print(*sorted(a)[:2])

#------------------------------задача----------------------------------#

## Поменять местами наибольший и наименьший элементы массива

s = input().split()
s_new = []
for num in s:
    s_new.append(int(num))
s_max = max(s_new)
s_min = min(s_new)
s_max_index = s_new.index(s_max)
s_min_index = s_new.index(s_min)
s_new[s_max_index], s_new[s_min_index] = s_new[s_min_index], s_new[s_max_index]
print(s_new)

#------------------------------задача----------------------------------#

# Найти наиболее часто встречающийся элемент в массиве целых чисел.

s = input()
counter = 0
x = ''
for el in range(len(s)):
    s1 = s.count(s[el])
    if s1 >= counter:
        counter = s1
        x = s[el]
print(x)