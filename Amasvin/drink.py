# Drink
    # name
    # price
    # cup_size
    # sugar : 당도
    # ice
# Drink <- Coffee
# Drink <- Bubbletea
    # pearl

# 옵션들
# 컵사이즈 : 레귤러, 점보
# 펄 : 타피오카, 알로에, 곤약, 코코넛
# 얼음량 : 적게, 기본, 많이, 없음
# 당도 : 30%, 50%, 70%, 100%


class Drink :
    # 클래스 변수 
    _CUP_SIZES = ('레귤러', '점보')  # 0:레귤러, 1:점보
    _SUGARS = ('30%', '50%', '70%', '100%') # 0:30%, 1:50% ...
    _ICES = ('없음', '적게', '기본', '많게')
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup_size = 0   #0:레귤러, 1:점보
        self.sugar = 1 #0:없음, 1:적게, 2:기본, 3:많게
        self.ice = 2    #0:30%, 1:50%, 2:70%, 3:100%
    def __str__(self):
        return f'이름 : {self.name}\t가격 : {self.price}원\t 컵 사이즈 : {Drink._CUP_SIZES[self.cup_size]}\t 당도 : {Drink._SUGARS[self.sugar]}\t 얼음량 : {Drink._ICES[self.ice]}'

    def set_cup_size(self):
        # 사용자에게 숫자 묻기 → 1:레귤러, 2:점보
        for index, cup_size_label in enumerate(Drink._CUP_SIZES):
            print(f'{index+1}.{cup_size_label}')
        cup_size = input('컵사이즈를 선택하세요: ')   # input으로 넣으면 숫자를 넣더라도 문자열로 받아들임
        if cup_size == '':  # 엔터 치면 기본값
            self.cup_size = 0
        else:
            self.cup_size = int(cup_size)-1 # 숫자를 제대로 입력했을 때
        #self.cup_size가 점보(2)일 때, 가격 +500원
        if self.cup_size == 1:
            self.price += 500

    def set_sugar(self):
        # 옵션 보여주기 1. 30%, 2. 50%...
        for index, sugar_label in enumerate(Drink._SUGARS):
            print(f'{index+1}.{sugar_label}')
        # 사용자 입력 받기
        sugar = input('당도를 선택하세요: ')
        # 그냥 엔터만, 기본값 : 1
        if sugar == '':
            self.sugar = 1
        # 숫자 입력하면, -1 -> index 바꿔주기
        else:
            self.sugar = int(sugar)-1
    def set_ice(self):
        for index, ice_label in enumerate(Drink._ICES):
            print(f'{index+1}.{ice_label}')
        ice = input('얼음량을 선택하세요: ')
        if ice == '':
            self.ice = 2
        else :
            self.ice = int(ice)-1

    def order(self):
        self.set_cup_size()
        self.set_sugar()
        self.set_ice()

if __name__ == '__main__':  # 시험 문제 100% 낼 거임
    음료1 = Drink("아메리카노", 1800)
    # 음료1.set_cup_size()
    # 음료1.set_sugar()
    # 음료1.set_ice()
    음료1.order()
    print(음료1)