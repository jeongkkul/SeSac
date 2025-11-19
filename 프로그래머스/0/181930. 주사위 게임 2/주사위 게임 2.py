def solution(a, b, c):
    sum1 = a + b + c
    sum2 = a*a + b*b + c*c
    sum3 = a*a*a + b*b*b + c*c*c

    # 모두 같음
    if a == b == c:
        return sum1 * sum2 * sum3
    
    # 두 개만 같음 (중복 1쌍)
    if a == b or b == c or a == c:
        return sum1 * sum2
    
    # 모두 다름
    return sum1
