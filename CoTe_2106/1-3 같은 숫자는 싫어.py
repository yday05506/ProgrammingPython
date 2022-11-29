def solution(arr):
    answer = []
    # arr 하나씩꺼내 쓸 때, 같은 숫자가 나오면 넘어가고 다른 숫자가 나오면 answer에 추가
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

result = solution([1,1,3,3,0,1,1])
print(result)   #[1,3,0,1]
result = solution([4,4,4,3,3])
print(result)   #[4,3]