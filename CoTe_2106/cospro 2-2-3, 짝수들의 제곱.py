def solution(N, M):
    answer = 0

    for i in range(N, M+1):
        if (i % 2 == 0):
            answer += i * i
    return answer

result = solution(4, 7)
print(result)