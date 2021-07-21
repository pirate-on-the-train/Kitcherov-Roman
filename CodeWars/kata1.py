# Телефонный номер

def create_phone_number(n):
    answer = ''
    for digit in n:
        answer += str(digit)
    return("(" + answer[:3] + ") " + answer[3:6] + "-" + answer[6:])

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#(123) 456-7890