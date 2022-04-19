greeting = 'hello'
to = 'world!'
say_hello = greeting + ', ' + to
print(say_hello)
print(greeting * 5)
print(greeting + '\n' + to)
print("\"" + greeting + "\"")   # 같은 따옴표를 쓰려면 역슬래시를 앞에 써준다
print('\'' + greeting + '\'')   # ''', """는 여러 줄 문자열 -> 보통 여러 줄 주석으로 씀
names = '''양다연
인소리
이예진
'''
print(names)


# *** 시험 문제 100% 나옴!!!
# indexing, slicing
names = '양다연인소리이예진'

# indexing : 하나만 꺼냄
print(names[2]) # '연'
print(names[4]) # '소'
print(names[8]) # '진'
print(names[-1])    # '진'
print(names[-2])    # '예'
print(names[-9])    # '양'
student_number = '2112'
print(student_number[0] + '학년')
print(f'{student_number[0]}학년')
print(f'{student_number[1]}반')

# slicing
print(names[2:5])   # [2] ~ [4]
print(names[2:4])   # 연인
print(names[-7:-5]) # 연인
print(names[4:7])   # 소리이
print(names[7:9])   # 예진
print(f'{student_number[2:4]}번')
print(f'{student_number[-2:]}번')   # start:end-1   [start:] = 끝까지
print(f'{student_number[0:-2]}학년반')
print(f'{student_number[:-2]}학년반')  # start:end-1   [:end-1] = 처음부터
print(f'{student_number[:]}')   # start:end-1   [:] = 앞 ~ 끝까지