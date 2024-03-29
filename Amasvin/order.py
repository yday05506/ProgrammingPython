from copy import copy

from coffee import Coffee
from bubbletea import BubbleTea

class Order:
    def __init__(self):
        self.menu = []  # 메뉴판
        self.init_menu()    # 메뉴판 초기화
        self.order_menu = []    # 주문한 음료수 리스트
    def __str__(self):
        # self.order_menu에서 drnk 하나씩 꺼내서 출력
        # 총 주문 금액 출력
        total_price = 0
        for drink in self.order_menu:
            total_price += drink.price
        return '\n'.join(str(drink) for drink in self.order_menu) + f'\n총 주문 금액은 {total_price}원입니다.'
    
    # 메뉴판 초기화
    def init_menu(self):
        new_menu = BubbleTea("하동녹차오레오", 4500)
        self.menu.append(new_menu)  # 리스트에 추가 : append()
        new_menu = Coffee("카페 모카", 3000)
        self.menu.append(new_menu)
        new_menu = BubbleTea("라즈베리소다", 2900)
        self.menu.append(new_menu)
    
    def order(self):
        #반복
        while True:
            self.show_menu()  # 메뉴판 보여주기
            # 음료수 고르기(사용자 입력 받기)
            choice = input("원하는 음료수를 고르세요(엔터 치면 끝) : ")
            # 엔터 치면 끝
            if choice == '':
                break
            # 새로운 음료수로 생성, 옵션들 주문
            new_drink = copy(self.menu[int(choice) - 1])
                # 메뉴 그대로 가져오면, 옵션에 따라 메뉴가 바뀌어 있음
                # 메뉴는 기본으로 놔두고, 복사해와서 그것의 옵션을 바꾸자
            new_drink.order()   # 음료 주문 받기(옵션)
            # print(new_drink)
            # 주문한 음료수 리스트에 새로운 음료수 추가
            self.order_menu.append(new_drink)
        # 주문한 음료수 리스트 출력
        print("-"*80)
        print("주문하신 음료수는 다음과 같습니다.")
        print(self) # __str__() 호출
        
    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index+1}. {drink.name}\t{drink.price}')

if __name__ == '__main__':
    order = Order()
    order.order()