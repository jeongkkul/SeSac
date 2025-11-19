def solution(arr, k):
    answer = []
    for x in arr:
        if k % 2 == 1:  # 홀수
            answer.append(x * k)
        else:           # 짝수
            answer.append(x + k)
    return answer
