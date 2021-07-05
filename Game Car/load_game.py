import pickle

file = open('save_people.pickle', 'rb')
man = pickle.load(file)
print(man)