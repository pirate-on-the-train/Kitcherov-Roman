# функция принимает список чисел, удвоить все элементы и вернуть

def RomanDouble(n):
    d = []
    for i in n:
        d.append(i * 2)
    return d

def ArtemDouble(n):
    return [i * 2 for i in n]

print(RomanDouble([1, 4, 8]))