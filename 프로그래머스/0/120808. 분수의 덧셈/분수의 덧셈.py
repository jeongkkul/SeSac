# # 첫 코드
# # 생각 정리
# # 1. denom1 과 denom2의 공배수 구하기
# # 공배수가 되기 위해 분모에 곱한 값이 있으면 해당 분자에도 곱하기
# # 출력시에는 [numer1 + numer2 , denom의 공배수 ]

# def solution(numer1, denom1, numer2, denom2):
#     answer = []
    
#     if denom1 % denom2 == 0 :
#         numer3 = numer1 * (denom1 // denom2)
#         denom3 = denom1 * (denom1 // denom2)
        
#         return [ numer3 + numer2 , denom1]
        
#     elif denom2 % denom1 == 0 :
#         numer2 * (denom2 // denom1)
#         denom2 * (denom2 // denom1)
        
#         return [ numer1 + numer2 , denom1]
    
#     else : # denom1과 denom2의 공배수가 없어서 둘이 곱해야 할 때 
#         numer1 * denom2
#         denom1 * denom2
#         numer2 * denom1
#         numer2 * denom1
        
#         return []
    
    
#     return answer


def solution(numer1, denom1, numer2, denom2):
    # 1. 통분하기
    numerator = numer1 * denom2 + numer2 * denom1  # 분자 계산
    denominator = denom1 * denom2                  # 분모 계산

    # 2. 최대공약수(gcd) 직접 구하기
    gcd = 1
    for i in range(1, min(numerator, denominator) + 1):
        if numerator % i == 0 and denominator % i == 0:
            gcd = i

    # 3. 약분하기
    numerator = numerator // gcd
    denominator = denominator // gcd

    # 4. 결과 반환
    return [numerator, denominator]


