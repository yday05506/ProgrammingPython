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
        self.cup_size = '레귤러'
        self.sugar = '50%'
        self.ice = '기본'
    def __str__(self):
        return f'이름 : {self.name}\t가격 : {self.price}원\t 컵 사이즈 : {self.cup_size}\t 당도 : {self.sugar}\t 얼음량 : {self.ice}'

음료1 = Drink("아메리카노", 1800)
print(음료1)