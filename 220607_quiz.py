# 1. 휴대전화 번호 입력하면 -, /, 띄어쓰기 없애고 숫자만 출력
phone_number = '010-7240-4658'
print(phone_number.replace('-', ''))
print('-' * 20)


# 2. 학번 -> 학년, 반. 학과, 번호 출력하기
student_number = '2108'
# >> 2학년 1반 뉴미디어소프트웨어과 08번
major = ' '
if (student_number[1:2] == '1') | (student_number[1:2] == '2'):
    major = '뉴미디어소프트웨어과'
elif (student_number[1:2] == '3') | (student_number[1:2] == '4'):
    major = '뉴미디어웹솔루션과'
elif (student_number[1:2] == '5') | (student_number[1:2] == '6'):
    major = '뉴미디어디자인과'
print(f'{student_number[0:1]}학년 {student_number[1:2]}반 {major} {student_number[2:5]}번')
# >> 2학년 1반 뉴미디어소프트웨어과 8번
print(f'{student_number[0:1]}학년 {student_number[1:2]}반 {major} {student_number[3:5]}번')
# >> if문 안 쓰고
print('-' * 20)


# 3. 10자리 숫자보다 작은 숫자를 넣으면 각 자리의 숫자의 합계를 출력


# 4. 1~100까지 369 게임을 출력
for i in range(1, 101):
    s = str(i)
    cnt = 0
    for ii in s:
        if (ii == '3') | (ii == '6') | (ii == '9'):
            cnt += 1
        if cnt == 0:
            print(ii, end=' ')
        else:
            print(cnt*"짝", end=' ')