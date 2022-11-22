def solution(age):
    answer = ''
    # age를 문자화 하기
    age = str(age)
    # age에서 '0'이면 'a로 바꾸기
    age = age.replace('0', 'a')
    # age에서 '1'이면 'b로 바꾸기
    age = age.replace('1', 'b')
    # age에서 '2'이면 'c로 바꾸기
    age = age.replace('2', 'c')
    # age에서 '3'이면 'd로 바꾸기
    age = age.replace('3', 'd')
    # age에서 '4'이면 'e로 바꾸기
    age = age.replace('4', 'e')
    # age에서 '5'이면 'f로 바꾸기
    age = age.replace('5', 'f')
    # age에서 '6'이면 'g로 바꾸기
    age = age.replace('6', 'g')
    # age에서 '7'이면 'h로 바꾸기
    age = age.replace('7', 'h')
    # age에서 '8'이면 'i로 바꾸기
    age = age.replace('8', 'i')
    # age에서 '9'이면 'j로 바꾸기
    age = age.replace('9', 'j')

    # age를 answer에 넣기
    answer = age



result = solution(23)
print(result)   #"cd"
result = solution(51)
print(result)   #"fb"
result = solution(100)
print(result)   #"baa"