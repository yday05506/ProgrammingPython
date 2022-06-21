# 예약어 X
# snake_case
# 내장 함수와 이름이 같아도 에러는 안 나지만, 내장 함수를 호출할 수 없음
# def sum(x):
#     print(x)
#
a = sum([10, 20, 3])
print(a)
print('-' * 20)
'''
java 함수
접근제어자 리턴형 함수명(매개변수 1, 매개변수2) {
    return 값;
}

python 함수
def 함수명(매개변수 1, 매개변수 2):
    return 값
'''
def my_print(age):
    print("임정훈 : " + str(age) + "살입니다.")   #이름 : 살입니다.
    print("임정훈 :", age, "살입니다.")   #이름 : 살입니다.
    print(f'임정훈 : {age}살입니다.')
print(my_print(43))   # my_print() 실행, my_print()의 리턴값 출력

print('-' * 20)

def my_print2(name, age):
    print(name + ": " + str(age) + "살입니다.")   #이름 : 살입니다.
    print(name, ":", age, "살입니다.")   #이름 : 살입니다.
    print(f'{name} : {age}살입니다.')
print(my_print2('안유진', 20))   # my_print() 실행, my_print()의 리턴값 출력
print(my_print2(age = 20, name = '안유진'))   # argument 순서와 상관 없이 매개변수 이름을 쓰면 거기에 들어감

print('-' * 20)

def my_print3(name, age, group):
    print(name + ": " + str(age) + "살입니다." + group + " 소속입니다.")   #이름 : 살입니다.
    print(name, ":", age, "살입니다.", group, "소속입니다.")   #이름 : 살입니다.
    print(f'{name} : {age}살입니다. {group} 소속입니다.')
print(my_print3(age = 20, name = '안유진', group = '아이브'))   # argument 순서와 상관 없이 매개변수 이름을 쓰면 거기에 들어감
# print(my_print3('안유진', age = 20, '아이브'))   # 키워드 인자 뒤에는 계속 키워드 인자를 넣어주어야 함
print(my_print3('안유진', age = 20, group = '아이브'))   # 키워드 인자 뒤에는 계속 키워드 인자를 넣어주어야 함
print(my_print3('안유진', group = '아이브', age = 20))   # 위치 인자는 무조건 키워드 인자 앞에 있어야 함

print('-' * 20)

def my_print4(name, age, group = '아이브'):
    print(name + ": " + str(age) + "살입니다." + group + " 소속입니다.")   #이름 : 살입니다.
    print(name, ":", age, "살입니다.", group, "소속입니다.")   #이름 : 살입니다.
    print(f'{name} : {age}살입니다. {group} 소속입니다.')
print(my_print4('안유진', age = 20, group = '아이즈원'))   # 위치 인자는 무조건 키워드 인자 앞에 있어야 함

print('-' * 20)

# 가변인자
def my_print5(*args):   # args 자료형은 tuple
    print('정보 : ')
    for arg in args:
        print(arg)
my_print5('안유진', 20, '아이브', '러브다이브')

print('-' * 20)

def my_print6(name, *args):   # args 자료형은 tuple
    print(f'{name} 정보 : ')
    for arg in args:
        print(arg)
my_print6('안유진', 20, '아이브', '러브다이브')

print('-' * 20)

# def my_print7(name, age = 20, group):   #기본 값 있는 파라미터 뒤에는 무조건 기본 값 있는 파라미터
#     print(name + ": " + str(age) + "살입니다." + group + " 소속입니다.")   #이름 : 살입니다.
#     print(name, ":", age, "살입니다.", group, "소속입니다.")   #이름 : 살입니다.
#     print(f'{name} : {age}살입니다. {group} 소속입니다.')
# print(my_print7('안유진', group = '아이브'))   # 위치 인자는 무조건 키워드 인자 앞에 있어야 함


# gugudan() : 구구단 2단 출력하자
def gugudan():
    dan = 2
    for n in range(1, 9 + 1):   # 1 <= n <= 9
        print(f'{dan} x {n} = {dan*n}')
gugudan()
# gugudan(5) : 구구단 5단 출력하자
def gugudan1(dan):
    for n in range(1, 9 + 1):   # 1 <= n <= 9
        print(f'{dan} x {n} = {dan*n}')
gugudan1(5)

print('-' * 20)

def say(name, msg = '안녕하세요', feeling = '🐶🍮'):
    print(f'{name}, {msg} {feeling}')
say('가현')
say('가현', feeling='🐶🍮🐶🍮')

print('-' * 20)

# 문제 안 냄
def fn(a, b=[]):
    b.append(a)
    print(b)
fn(3)   # [3]
fn(5)   # [5] : x, [3, 5] : o
fn(10, [1]) # [1, 10]
fn(7)   # [3, 5, 7]

print('-' * 20)

say('현진', '미안해')

print('-' * 20)

# 지금부터 20년 후의 내 나이 리턴
def plus20 (age):
    # print(age+20)
    return age + 20
a = plus20(18)  # 38
print(a)    # None : plus20() return 값이 없어서 None 리턴

print('-' * 20)

# 전화번호 앞 자리(지역번호)와 맨 뒤 네 자리 출력
def tel(number):
    index = number.find('-')
    f = number[:index]
    b = number[-4:]
    return f, b
# front = '010'
# back = '5678'
front, back = tel('010-1234-5678')
print(f'앞 : {front}, 뒤 : {back}')

print('-' * 20)

def min_max(리스트):
    # max_value = 리스트[0]
    # min_value = 리스트[0]
    # for i in range(1, 6):
    #     if max_value > 리스트[i]:
    #         max_value = 리스트[i]
    #     if min_value < 리스트[i]:
    #         min_value = 리스트[i]
    # return max_value, min_value

    # return max(리스트), min(리스트 )

    min_v = 리스트[0]
    max_v = 리스트[0]
    for n in 리스트 :
        if min_v > n :
            min_v = n
        if max_v < n :
            max_v = n
    return min_v, max_v
min_value, max_value = min_max([3, 31, 1, 6, 5, -6])
print(f'최소 : {min_value}\t 최대 : {max_value}')