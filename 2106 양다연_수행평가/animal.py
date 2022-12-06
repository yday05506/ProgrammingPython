#2106 양다연

class 동물:
    def __init__(self, name):
        self.이름 = name
        self.다리수 = 0
        self.울음소리 = None

    def __str__(self):
        return f'이름: {self.이름}'

    def 울다(self):
        print(f'{self.이름}: {self.울음소리}')

if __name__ == '__main__':
    동물1 = 동물("드래곤")
    print(동물1)

#2106 양다연