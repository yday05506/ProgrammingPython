'''
조건식  = True 또는 False로 결정되는 문장
파이썬에서 if문 작성 시 유의해야 할 사항 - 콜론, 들여쓰기
'''

if True :
    print("실행")

#교통수단 결정 문제
money = 8000
if money >= 10000 :
    print("택시를 타라")
else :
    print("버스를 타라")

#input 함수
x = input()
print(x, type(x))
num = int(input())
print(num, type(num))

#교통수단 결정 문제 + input 함수
money = int(input('돈을 입력하시오 : '))
if money >= 10000 :
    print("택시를 타라")
else :
    print("버스를 타라")

#문제 1
num = int(input('숫자를 입력하시오 : '))
if num % 2 == 0 :
    print("짝수입니다")
else :
    print("홀수입니다")

#문제 2
password = input('암호 입력 : ')
if password == '미림과학고' :
    print("암호이다")
else :
    print("암호가 아니다")