'''
Цикл while

Цикл - некий повтор алгоритма

Один из примеров - while

while - ПОКА

Шаблон:

while УСЛОВИЕ:
    КОД
    С
    ОТСТУПОМ

УСЛОВИЕ - ТО, ОТ ЧЕГО ЗАВИСИТ ЦИКЛ

Пример:
'''
a = 0
while a < 100:
    a += 1
    print(str(a) + '. Я буду прилежно учиться')

a = 0
while True:
    a += 1
    print(a)
    if a == 100:
        break

# написать скрипт для поиска факториала числа
a = int(input())
i = 1
fact = 1
while i <= a:
    fact *= i
    i += 1
print('{0}! = {1}'.format(a, fact))