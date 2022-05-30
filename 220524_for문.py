#문자열
for ch in "SORI" :
    print(ch, end="*")
    print()


#리스트
for item in["힙합", "발라드"] :
    print(item)


#튜플
for item in (2929, 39393) :
    print(item)
for a, b in ((12, 33), (2, 35)):
    print(a, b) #패킹 언패킹


#set
for item in {"WSM", "JAVA", "Python"} :
    print(item)


#dictionary
pl = {"C":1972, "JAVA":1995, "Python":1991}
for item in pl:
    print(item)
for key in pl.keys():
    print(key)  #위 결과와 동일
for val in pl.values():
    print(val)  #값만 출력
for key, val in pl.items():
    print(key, val) #키, 값 둘 다 출력


#문제 1
num_list = [-5, 127, -13, 9, -21, 100]
for num in num_list:
    if num > 0:
        print(num)


#짝수, 홀수
num_list = [13, 8, 7, 55, 100, 2, 12, 10, 17]
for num in num_list :
    if num % 2 == 0 :
        print(f'{num}은 짝수이다')
    else :
        print(f'{num}은 홀수이다')

holzzak = ["짝수", "홀수"]
for num in num_list:
    print(f'{num}은 {holzzak[num%2]}이다')


#자리 수
for num in num_list:
    print(f'{num}은 {len(str(num))}자리 수이다')


#문제 2
test_score = {"에스쿱스":90, "정한":100, "조슈아":95, "준":50, "호시":85, "원우":80, "우지":75, "도겸":65, "민규":45, "디에잇":30, "승관":85, "버논":30, "디노":25}
p = ["합격", "불합격"]
for name, score in test_score.items():
    print(f'{name}은/는 {p[score>=60]}입니다.')


#range() 함수
print(list(range(0, 10, 1)))
print(list(range(10, 0, -1)))
print(list(range(0, 10, 5)))
print(list(range(0, 10)))   #증감 기본 : 1
print(list(range(10)))  #시작 기본 : 0


#리스트
nctdream = ['런쥔', '제노', '해찬', '마크', '재민', '지성', '천러']
for member in nctdream:
    print(member)

for i in range(0, len(nctdream)):
    print(i+1, nctdream[i])

for i, member in enumerate(nctdream):
    print(i+1, member)


#문제 3
total = 0
for num in range(1, 200):
    if num % 3 == 0:
        total += num
print(f'3의 배수의 합 : {total}')

total = 0
for num in range(0, 200, 3):
    total += num
print(f'3의 배수의 합 : {total}')    #위와 결과 같음

total = 0
for num in range(500, 1000, 5):
    total += num
print(f'5의 배수의 합 : {total}')

print(sum(list(range(500, 1000, 5))))   #위와 결과 같음


#sum() 함수, max, min
l = [1, 2, 3, 4, 5]
print(sum(l))
print(max(l))
print(min(l))


#문제 4
for gugudan in range(1, 10):
    print(f'2x{gugudan}={2*gugudan}')


#문제 5
for gugudan in range(2, 10):
    for gugudan1 in range(1, 10):
        print(f'{gugudan}x{gugudan1}={gugudan*gugudan1}')