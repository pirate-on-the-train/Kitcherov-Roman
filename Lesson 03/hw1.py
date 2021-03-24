# Домашняя задача через цикл while

order = []
a = ''

while a != '0':
    a = input('Введите блюдо: ')
    if a != '0':
        order.append(a)

i = 0
while i < len(order):
    print(str(i + 1) + '. ' + order[i])
    i += 1