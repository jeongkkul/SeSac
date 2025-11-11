# # 내 코드 
# # 생각 과정
# # len(numlist) // n = result, result차원 

# # 예시로 작성해본 것
# # num_list = [1,2,3,4,5,6,7,8]
# # len(num_list)


# # answer =[ 
# #           [num_list[0], num_list[1]], 
# #           [num_list[2], num_list[3]], 
# #           [num_list[4], num_list[5]], 
# #           [num_list[6], num_list[7]]
# #         ]
# # answer

# def solution(num_list, n):
#     lf num_list // n == 0 :
#         for i in range(0, len(num_list)) :
#             num_list[i], num_list[]
            
        
        
#     answer = [[]]
    
    
    
    
#     return answer


# # 위에 적은 것들 지우지 말고 주석처리하기



def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]


# 다른 방법의 코드
# def solution(num_list, n):
#     answer = []
#     for i in range(0, len(num_list), n):   # 0부터 n씩 건너뛰며
#         group = num_list[i:i+n]            # n개씩 자르기
#         answer.append(group)               # 자른 걸 리스트에 추가
#     return answer


