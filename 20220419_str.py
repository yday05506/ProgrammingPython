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


# 문자열 함수
print(f'길이 : {len(student_number)}')    # 길이 : 4
print(f'2 개수 : {student_number.count("2")}')   # 특정 문자열이 몇 개 있는지
print(f'{"NCT dream darling".upper()}') # 대문자
print(f'{"NCT dream darling".lower()}') # 소문자
s = "    NCT dream buffering    "
print(f'{s.strip()}')   # 띄어쓰기가 없어짐
print(f'{s.lstrip()}')   # 왼쪽 띄어쓰기가 없어짐
print(f'{s.rstrip()}')   # 오른쪽 띄어쓰기가 없어짐
print(f'{s.find("e")}') # 인덱스를 찾아줌 : 8
print(f'{s.find("z")}') # 없으면 -1
print(f'{s.rfind("e")}') # 17
print(f'{s.count("e")}')    # 2
print(f'{s.index("d")}')    # 8
# print(f'{s.index("z")}')    # 없으면 ValueError : substring not found
print(f'{s.replace("buffering", "hello future")}')  # replace 하면 바뀐 문자열 리턴하지만 원본은 바뀌지 않음
print(s)

print('e' in s) # True  s 문자열 안에 e가 있는가
print('z' in s) # False s 문자열 안에 z가 있는가


# split, join
ip = '10.253.123.119'
ip_list = ip.split('.') # .으로 문자열 나눔
print(ip_list)
names = '양다연, 최자윤, 임채영, 이예진, 인소리'
name_list = names.split(', ')
print(name_list)
print(name_list[2]) # 임채영
print(name_list[2:4])   # 임채영, 이예진
ip_list_str = '::'.join(ip_list)    # list에서 하나씩 꺼내서 ::으로 연결
print(ip_list_str)
name_list_str = ' | '.join(name_list)
print(name_list_str)
print(", ".join(name_list))