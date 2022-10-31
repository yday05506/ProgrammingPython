class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f'{self.name}, {self.age}, {self.gender}'

    def __del__(self):
        print(f'나의 죽음을 알리지 말라')

a = Human("다연", 18, "여자")
print(a)
del(a)

class Car:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
car = Car(2, 1000)
print(car.바퀴)
print(car.가격)