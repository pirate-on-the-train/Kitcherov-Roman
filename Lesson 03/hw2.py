# Домашняя задача через цикл for

order = []
a = ''

while a != '0':
    a = input('Введите блюдо: ')
    if a != '0':
        order.append(a)


for i in range(len(order)):
    print(str(i + 1) + '. ' + order[i])