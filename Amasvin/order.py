from coffee import Coffee
from bubbletea import BubbleTea

class Order:
    def __init__(self):
        self.menu = []  # 메뉴판
        self.init_menu()    # 메뉴판 초기화
        self.order_menu = []    # 주문한 음료수 리스트
    def __str__(self):
        pass
    
    # 메뉴판 초기화
    def init_menu(self):
        new_menu = BubbleTea("하동녹차오레오", 4500)
        self.menu.append(new_menu)
        new_menu = Coffee("카페 모카", 3000)
        self.menu.append(new_menu)
        new_menu = BubbleTea("라즈베리소다", 2900)
        self.menu.append(new_menu)
    
    def order(self):
        #반복
            self.show_menu()  # 메뉴판 보여주기
            # 음료수 고르기(사용자 입력 받기)
            # 새로운 음료수로 생성, 옵션들 주문
            # 주문한 음료수 리스트에 새로운 음료수 추가
        # 주문한 음료수 리스트 출력
        
    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index+1}. {drink.name}\t{drink.price}')

if __name__ == '__main__':
    order = Order()
    order.show_menu()