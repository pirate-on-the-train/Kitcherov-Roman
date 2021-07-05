'''
# 1 способ

a = input('Введите число: ')

file = open('save.txt', 'w')
file.write(a)
file.write('4')
file.write('3')
file.write('2')
file.write('1')
file.write('6')
file.write('5')
file.close()
'''

# 2 способ

import pickle
people1 = {
    'name' : 'Nikodim',
    'age' : 25,
    'city' : 'Novosibirsk'
}

file1 = open('save_people.pickle', 'wb')
pickle.dump(people1, file1)
file1.close()