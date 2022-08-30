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