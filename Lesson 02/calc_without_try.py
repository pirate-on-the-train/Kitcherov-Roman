action = input()
a = int(input())
b = int(input())
if action == '+':
    print(a + b)
elif action == '-':
    print(a - b)
elif action == '*':
    print(a * b)
elif action == '/':
    if b == 0:
        print('Нельзя делить на 0')
    else:
        print(a / b)