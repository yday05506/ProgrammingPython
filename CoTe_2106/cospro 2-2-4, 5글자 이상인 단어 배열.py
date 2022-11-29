def solution(words):
    answer = ''
    #words를 하나씩 꺼내어 words에 넣기
    for word in words:
        #word가 글자수가 홀수이면 answer에 추가
        if len(word) % 2 == 1:
            answer += word

    return answer


words1 = ["my", "favorite", "color", "is", "violet"]
result1 = solution(words1)
print(result1) # "myfavoritecolorisviolet"

words2 = ["yes", "i", "am"]
result2 = solution(words2)
print(result2) # "empty"