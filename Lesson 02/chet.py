# Написать скрипт, который возводит 
# чётное число в квадрат, а нечётное 
# в куб

a = int(input())    # Считать с клавиатуры данные, перевести их в целые числа, записать в переменную a
if a % 2 == 0:      # если остаток от деления a на 2 равен 0, то (грубо говоря, если число чётное) 
    print(a ** 2)   # выводим на экран a во 2 степени
else:               # иначе (если нечётное)
    print(a ** 3)   # выводим на экран a в 3 степени