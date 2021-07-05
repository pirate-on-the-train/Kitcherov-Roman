# Создать класс машина
# Реализовать в нём методы Ехать(НаСколько) и свойства для бензина, скорости и координаты
# 1 поездка на 10 км тратит 1 литр бензина

class Car():
    def __init__(self, gasoline, speed, xPos):
        self.gasoline = gasoline
        self.speed = speed
        self.xPos = xPos
    
    def Drive(self, HowMuch):
        self.xPos += HowMuch
        self.gasoline -= HowMuch / 10

        # 10 км = 1 литр 
        # HowMuch = 15 / 10 = gas
        # gas = 1,5 литра
    
car = Car(100, 30, 0)
car.Drive(30)
input()
