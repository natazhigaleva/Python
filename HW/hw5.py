#-----------------------------------Задача----------------------------------------#
# Дано 3 стороны треугольника
# Проверить существует ли треугольник
#
a = int(input())
b = int(input())
c = int(input())
if (a + b) > c or (b + c) > a or (a + c) > b:
    print("YES")
else:
    print("NO")
#
C:\Users\jigal\AppData\Local\Programs\Python\Python311\python.exe C:\Users\jigal\PycharmProjects\pythonProject\main.py 
3
2
5
YES

Process finished with exit code 0


#-------------------------ЗАДАЧА ПОИСК ОШИБОК(BEFORE)-----------------------------#
# калькулятор
# доступны операции умножить и поделить
num1 = 5
operation = '*'
num2 = 6
if operation == '*':
    print(num1/num2)
if operation == '/':
    print(num1/num2)
else:
    print("нет такой операции")

#-------------------------ЗАДАЧА ПОИСК ОШИБОК(AFTER)-----------------------------#
# калькулятор
# доступны операции умножить и поделить
num1 = float(input())  # задаем тип переменной
num2 = float(input())  # задаем тип переменной
operation = str(input(''))  # задаем тип переменной
if operation == '*':
    print(num1 * num2)  # операция деления исправлена на умножение
if operation == '/':    
    if num2 == 0:  # добавлена проверка деления на ноль
        print("На ноль делить нельзя!")
    else:
        print(num1 / num2)
else:
    print("нет такой операции")
#


#------------------------------ЗАДАЧА----------------------------------#
#Дано:
# * кол-во цифр в пароле (не делать проверку на отрицательность)
# * кол-во малых букв в пароле (не делать проверку на отрицательность)
# * кол-во заглавных букв в пароле (не делать проверку на отрицательность)
# * кол-во запрещенных символов в пароле (не делать проверку на отрицательность)
# Для использования пароля необходимо:
# * минимум 1 цифру, 1 малую букву, 1 заглавную букву
# * в пароле не должно быть запрещенных символов
# * минимальная длина пароля 6 символов
# Написать можно ли использовать такой пароль
#
count_num = 1  # только число
count_under = 1  # строка 
count_upper = 1  # строка
count_ban = 0  
count_symbols = 6  # строка
if count_symbols => 6 and count_ban == 0:
    if count_num => 1 and count_under => 1 and count_upper => 1:
        print("Пароль можно использовать")
    else:
        print("Пароль использовать нельзя")
else:
    print("Пароль использовать нельзя")
#-------------------------------------------------------------------------#