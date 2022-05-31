'''
JAVA
while(조건식) {
    실행문;
    증감식;
}

python
while 조건식 :
    실행문
    증감식
'''
x = 3
while x < 5:
    print(x)    # 무한루프 멈추는 방법 : ctrl + c -> 파이참에선 안 되지만 시험에선 낼 거임 ㅋ
    x += 1
print("-" * 20)

# echo = input()
# while echo != 'exit':
#     print(echo)
#     echo = input()
echo = input()
while True: # 무한 루프
    if echo == 'exit':  # 탈출 조건
        break
    print(echo)
    echo = input()
print("-" * 20)