def solution(array):
    answer = 0
    #array를 정렬하기
    array.sort()
    #중앙값 구하기
    #5개일 때 2번 인덱스, 3개일 때 1번 인덱스
    answer = array[len(array)//2]
    return answer

print(solution([1,2,7,9,11]))   #7
print(solution([9, -1, 0])) #0