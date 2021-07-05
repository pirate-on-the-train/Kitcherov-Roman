"""
Иподром

Есть лошади, они имеют параметры скорости и растояние, которое пробежали.
"""

import random, os, time

class horse():
    distance = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def run(self):
        self.distance += self.speed

    def info(self):        
        return f"{self.name} прошёл {self.distance} ({round(self.distance / d * 100)} %)"

d = int(input("Введите расстояние: "))
count = int(input("Сколько лошадей участвует: "))
horse_list = []


for i in range(count):
    horse_list.append(horse(i + 1, random.randint(5, 20)))

os.system('cls||clear')
for i in range(3, 0, -1):
    print(f"Старт гонки через: {i}")
    time.sleep(1)
    os.system('cls||clear')

done = False
while not done:
    for h in horse_list:
        h.run()
        if h.distance >= d:
            print(f"Победила лошадь {h.name}")
            done = True
        else:
            print(h.info())
    if done:
        break
    else:
        time.sleep(1)
        os.system('cls||clear')

input()
    