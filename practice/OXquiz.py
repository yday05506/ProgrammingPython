def solution(quiz):
    answer = []

    for i in quiz:
        c = i.split('=')
        for j in range(len(c)):
            if eval(c[0]) == eval(c[1]):
                answer.append('O')
                break
            else:
                answer.append('X')
                break

    return answer
