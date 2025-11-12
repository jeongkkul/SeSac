# # 첫 코드
# # 정수 배열에 들어있는 요소를 전부 문자열로 바꾸자. str
# # 그리고 각 문자열을 하나씩 뽑아서 인덱싱한 값에서 ==7 인 결과만 다른 리스트에 집어넣자
# # 마지막으로 len함수 이용해서 

# def solution(array):
#     answer = 0

#     for i in range(len(array)) : 
#         k=0
#         cnt = 0
#         i[k] == 7
#         k +=1
#         cnt +=1
        
#         answer = cnt 
        
#     return answer


def solution(array):
    count = 0
    
    for num in array:
        # 숫자를 문자열로 변환한 뒤, 문자열 안의 '7' 개수를 세기
        count += str(num).count('7')
        
    return count
