#2106 양다연

from animal import 동물

class 돼지(동물):
    def __init__(self, name):
        super().__init__(name)
        self.다리수 = 4
        self.특징 = "돼지코"
        self.울음소리 = "꿀꿀"

    def __str__(self):
        return super().__str__() + f', 특징: {self.특징}, 다리수: {self.다리수}개'

if __name__ == '__main__':
    동물2 = 돼지("저팔계")
    동물2.울다()
    print(동물2)

#2106 양다연