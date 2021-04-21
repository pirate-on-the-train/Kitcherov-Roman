# Написать калькулятор, но через функции

def Sum(a, b):
    return a + b

def Sub(a, b):
    return a - b

def Mult(a, b):
    return a * b

def Div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: Деление на 0"

def Calc(a, sign, b):
    if sign == '+':
        print('{0} {1} {2} = {3}'.format(a, sign, b, Sum(a, b)))
    elif sign == '-':
        print('{0} {1} {2} = {3}'.format(a, sign, b, Sub(a, b)))
    elif sign == '*':
        print('{0} {1} {2} = {3}'.format(a, sign, b, Mult(a, b)))
    elif sign == '/':
        print('{0} {1} {2} = {3}'.format(a, sign, b, Div(a, b)))
try:
    first = int(input('Введите первое число: '))
    sign = input('Введите знак: ')
    second = int(input('Введите второе число: '))
    Calc(first, sign, second)
except ValueError:
    print('Вводить нужно числа')