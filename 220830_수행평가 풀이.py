# 1. 전화번호를 인자로 받아, 각 숫자 중 홀수만 더해서 합계를 리턴하는 sum_odd 함수를 작성하시오.
def sum_odd(phone_number):
    sum_value = 0
    # 전화번호에서 하나씩 꺼내기
    for number in phone_number:
        # 문자 -> 숫자
        number = int(number)
        # 홀수 구하기
        if number % 2 != 0:
            # 합계 구하기
            sum_value += number
    print(sum_value)
result = sum_odd('01088792517')
print(result)

def sum_odd2(phone_number):
    return sum([int(number) for number in phone_number if int(number) % 2 != 0])
result = sum_odd2('01088792517')
print(result)
print('----------')


# 2. 영단어를 인자로 받아, 모음인 a, e, i, o, u만 *로 대체하여 리턴하는 encrypt 함수를 작성하시오.
def encrypt(word):
    result = ''
    for char in word:
        # 모음인지 구별하기
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            # 별로 바꾸기
            char = '*'
            result += char
        # 다르면
        else:
            # 그대로 쓰기
            result += char
    return result
print(encrypt('ive'))
print('----------')


# 3. 십진수를 2진수로 바꾸시오.
def dec_to_bin(number):
    # return bin(number)[2:]
    # return bin(number).replace('0b', '')
    # share : 몫, number : 나머지
    s = ''
    # 무한 반복
    while True:
        # number가 0이면 끝내고 결과 리턴
        if number == 0:
            return s
        # 아니면 number를 2로 나눈 나머지를 앞으로 보관 s = '1' + s
        else:
            reminder = number % 2
            s = str(reminder) + s
            # number는 number를 2로 나눈 몫으로 설정
            number = number // 2

print(dec_to_bin(10))   #1010
print(dec_to_bin(2))   #10
print(dec_to_bin(77))   #1001101
print(dec_to_bin(1024))   #10000000000
print('----------')


# 4. 이니셜 abbreviate
def abbreviate(name):
    name = name.strip()
    # 한 글자씩 꺼내기(반복문)
    for index, spell in enumerate(name):
        # 첫 번째 글자 -> 대문자 -> 저장
        if index == 0:
            result = spell.upper() + '. '
        # 띄어쓰기 -> 한 칸 뒤에 있는 글자 -> 대문자 -> 저장
        if spell == ' ':
            result += name[index + 1].upper() + '. '
    return result.strip()
print(abbreviate('Maverick'))   # M.
print(abbreviate('HAE CHAN'))   # H. C.
print(abbreviate('jin young park'))   # J. Y. P.


def abbreviate2(name):
    result = '. '.join([word[0].upper() for word in name.split()])   # 단어를 잘라서 list에 넣어줌
    return result + '.'
# print(abbreviate2('Maverick'))   # M.
# print(abbreviate2('HAE CHAN'))   # H. C.
print(abbreviate2('jin young park'))   # J. Y. P.
print('----------')


# 5. 사용한 시간(분)을 인자로 받아 PC방 요금을 리턴
def fare_pc(minutes):
    # minutes을 10으로 나누자. 몫
    share = minutes // 10
    # 몫 * 1000 = 요금
    fare = share * 1000
    # minutes를 10으로 나눈 나머지가 있으면, +1000
    if minutes % 10 != 0 :
        fare += 1000
    return fare
print(fare_pc(10))
print(fare_pc(30))
print(fare_pc(60))
print(fare_pc(62))