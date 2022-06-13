# 1. 휴대전화 번호 입력하면 -, /, 띄어쓰기 없애고 숫자만 출력
phone_number = '010-7240-4658'
print(phone_number.replace('-', ''))
print('-' * 20)


# 2. 학번 -> 학년, 반. 학과, 번호 출력하기
student_number = '2108'

# >> 2학년 1반 뉴미디어소프트웨어과 08번
if (student_number[1] == '1') | (student_number[1] == '2'):
    major = '뉴미디어소프트웨어과'
elif (student_number[1] == '3') | (student_number[1] == '4'):
    major = '뉴미디어웹솔루션과'
elif (student_number[1] == '5') | (student_number[1] == '6'):
    major = '뉴미디어디자인과'
print(f'{student_number[0]}학년 {student_number[1]}반 {major} {student_number[2:]}번')

# >> 2학년 1반 뉴미디어소프트웨어과 8번
print(f'{student_number[0]}학년 {student_number[1]}반 {major} {int(student_number[2:])}번')

# >> if문 안 쓰고
majors = ['뉴미디어소프트웨어과', '뉴미디어소프트웨어과', '뉴미디어웹솔루션과','뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
index = int(student_number[1])
major = majors[index-1]
print(f'{student_number[0]}학년 {student_number[1]}반 {major} {int(student_number[2:])}번')
print('-' * 20)


# 3. 10자리 숫자보다 작은 숫자를 넣으면 각 자리의 숫자의 합계를 출력
number = 331
n1 = int(number % 1000 / 100)
n2 = int(number % 100 / 10)
n3 = int(number % 10)
print(n1 + n2 + n3)
# >> 7

number = 523523
sum_val = 0
while True: #while number != 0
    if number == 0:
        break
    sum_val += number % 10
    number = number // 10
print(sum_val)

#문자 한 자리씩 빼서 계산
number = 523523
number_s = str(number)  #523523
sum_val2 = 0
for n in number_s:
    sum_val2 += int(n)
print(sum_val2)
# >> 20
# -> 이게 더 파이썬 같은 코드

sum_val3 = 0
for index in range(len(number_s)):
    sum_val3 += int(number_s[index])
print(sum_val3)
# >> 20
# -> 자바 같은 코드

# 나머지 = number % 10   # 3
# number = number // 10   #523523 -> 52352
# 나머지 = number % 10   # 2
# number = number // 10   #523523 -> 5235
# 나머지 = number % 10   # 5
# number = number // 10   #523523 -> 523
# 나머지 = number % 10   # 3
# number = number // 10   #523523 -> 52
# 나머지 = number % 10   # 2
# number = number // 10   #523523 -> 5
# 나머지 = number % 10   # 5
# number = number // 10   #523523 -> 0
print('-' * 20)


# 4. 1~100까지 369 게임을 출력
for i in range(1, 101):
    s = str(i)
    cnt = 0
    for ii in s:
        if (ii == '3') | (ii == '6') | (ii == '9'):
            cnt += 1
        if cnt == 0:
            print(ii, end = ' ')
        else:
            print(cnt*"짝", end=' ')