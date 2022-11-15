from drink import Drink # 나와 같은 폴더에 있는 drink.py 파일에서 Drink 가져오기


class BubbleTea(Drink):
    # 클래스 변수
    _PEARLS = ('타피오카', '코코', '알로에', '곤약')
    def __init__(self, name, price):
        super().__init__(name, price)   # 부모의 생성자 호출    # 시험 100% 나옴!!
        self.pearl = 0  # 0:타피오카, 1:코코, 2:알로에, 3:곤약
        pass
    def __str__(self):
        return super().__str__() + f'\t펄 : {BubbleTea._PEARLS[self.pearl]}펄'

    def set_pearl(self):
        # 옵션 보여주기 1. 30%, 2. 50%...
        for index, pearl_label in enumerate(BubbleTea._PEARLS):
            print(f'{index + 1}.{pearl_label}펄')    # 1. 타피오카펄, ...
        # 사용자 입력 받기
        pearl = input('펄을 선택하세요: ')
        # 그냥 엔터만, 기본값 : 0
        # if pearl == '':
        #     self.pearl = 0
        # # 숫자 입력하면, -1 -> index 바꿔주기
        # else:
        #     self.pearl = int(pearl) - 1
        self.pearl = 0 if pearl == '' else int(pearl) - 1

    def order(self):
        # 부모 order() 호출
        super().order() # 컵사이즈, 당도, 얼음량 설정
        # 내 set_pearl() 호출
        self.set_pearl()

if __name__ == '__main__':  # *****
    버블티1 = BubbleTea('타로버블티', 3700)
    버블티1.order()
    print(버블티1)