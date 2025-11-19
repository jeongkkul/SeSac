def solution(myString):
    answer = ''
    for ch in myString:
        if ch < 'l':   # 'l'보다 앞이면
            answer += 'l'
        else:
            answer += ch
    return answer
