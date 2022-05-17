#교통수단 문제
money = int(input('돈을 입력하시오 : '))
if money >= 10000 :
    print("택시를 타라")
elif money >= 720 :
    print("버스를 타라")
else :
    print("그냥 걸어가라")


#문제 1
num = int(input('정수를 입력하시오 : '))
if num % 4 == 0 :
    print("4의 배수")
elif num % 3 == 0 :
    print("3의 배수")
elif num % 2 == 0 :
    print("2의 배수")

# 만약 12를 입력했을 때 다 출력하려면 if를 써야 함
if num % 4 == 0 :
    print("4의 배수")
if num % 3 == 0 :
    print("3의 배수")
if num % 2 == 0 :
    print("2의 배수")


#문제 2
age = int(input('나이를 입력하시오 : '))
if 10 <= age < 20 :
    print("10대")
elif 30 <= age < 40 :
    print("30대")
else :
    print("10대, 30대가 아님")

# 연산식으로 바꿈
print(str(age // 10 * 10) + "대")


#문제 3
x = int(input('정수를 입력하시오 : '))
if x > 10 and x % 2 == 0 :
    print("10 초과 짝수")
else :
    print("정수")


#문제 4
test = int(input('시험 점수를 입력하시오 : '))
if 90 <= test <= 100 :
    print("A")
elif 80 <= test :
    print("B")
elif 70 <= test :
    print("C")
elif 60 <= test :
    print("D")
elif 0 <= test :
    print("F")


#문제 5
mbti = input('MBTI 입력 : ')
if mbti.upper() == 'INFP' :
    print("블록체인형")
elif mbti.upper() == 'ISFP' :
    print("네트워크 개발자형")
else :
    print("아직 개발 중입니다.")


#문제 6
x = int(input('정수를 입력하시오 : '))
if x > 10 :
    if x % 2 == 0 :
        print("10 초과 짝수")
    else :
        print("10 초과 홀수")
elif x <= 10 :
    print("10 이하")


#문제 7
nickname = '양다연'
id = 'yde0506'
password = 'yde3424'
if input('ID : ') == id :
    if input('Password : ') == password :
        print(f'환영합니다, {nickname}님')
    else :
        print("패스워드가 틀렸습니다.")
else :
    print("알 수 없는 사용자입니다.")