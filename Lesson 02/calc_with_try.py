try:
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
        print(a / b)
except ZeroDivisionError:
    print('Нельзя делить на 0')
except ValueError:
    print('Нельзя вводить текст')