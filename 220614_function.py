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