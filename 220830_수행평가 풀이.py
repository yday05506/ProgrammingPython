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