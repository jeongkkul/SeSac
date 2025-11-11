def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):       # i부터 j까지 숫자 반복
        for ch in str(num):           # 숫자를 문자열로 바꿔 각 자리 확인
            if ch == str(k):          # k와 같은 문자인 경우
                answer += 1
    return answer
