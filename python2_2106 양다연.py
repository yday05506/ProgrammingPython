#1
# def sum_odd(num):
#     for arg in int(num):
#         if int(arg) % 2 == 1 :
#             arg += arg
# result = sum_odd('01012345678')
# print(result)

#2
# def encrypt(word):
#     for w in word:
#         if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u' :
#             w = '*'
# print(encrypt('ive'))

#3

#4
# def abbreviate(c):
#     for cc in c:
#         cc.split(" ")
# print(abbreviate("HAE CHAN"))

#5
def fare_pc(minute):
    money = 1000
    if minute // 10 == 0:
        return money * 1
    elif minute % 10 != 0 :
        return money * (minute // 10 + 1)
    else:
        return money * (minute // 10)
# print(fare_pc(minute=3))
# print(fare_pc(minute=20))
# print(fare_pc(minute=34))

#6
def get_bmi(height, weight):
    height = height / 100
    bmi = round(weight / (height * height), 2)
    if bmi < 18.5:
        print(f'저체중 {bmi}')
    elif bmi < 23:
        print(f'정상 {bmi}')
    elif bmi < 25:
        print(f'과체중 {bmi}')
    else:
        print(f'비만 {bmi}')
# print(get_bmi(height=170, weight=60))
# print(get_bmi(height=150, weight=60))
# print(get_bmi(height=180, weight=50))
# print(get_bmi(height=160, weight=60))

#7
# def minus_time(hour1, minute1, hour2, minute2):
#     for hour in range(0, 23+1):
#         hour = hour1 - hour2
#         for minute in range(0, 59+1):
#             minute = minute1 - minute2
# hour, minute = minus_time(hour1=13, minute1=40, hour2=6, minute2=33)
# print(hour, minute)

#8
# def rgb_to_hex(r, g, b):
#     r1 = str(hex(r))
#     g1 = str(hex(g))
#     b1 = str(hex(b))
#     print(f'#{r1[2:]}{g1[2:]}{b1[2:]}')
# print(rgb_to_hex(r=255, g=255, b=255))
# print(rgb_to_hex(r=255, g=0, b=255))
# print(rgb_to_hex(r=0, g=0, b=0))