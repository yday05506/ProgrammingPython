#2106 양다연

from animal import 동물

class 새(동물):
    def __init__(self, name):
        super().__init__(name)
        self.다리수 = 2

    def __str__(self):
        return super().__str__() + f', 다리수: {self.다리수}개'

    def set_울음소리(self, 울음소리):
        self.울음소리 = 울음소리

if __name__ == '__main__':
    동물3 = 새("해리")
    동물3.set_울음소리("개굴개굴개구리")
    동물3.울다()
    print(동물3)

#2106 양다연