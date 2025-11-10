# def solution(n):
#     answer = 0
    
#     # 약수 nums 개수 제한
    
#     nums_list = []
#     for nums in range(1, n+1) :
#     # nums_list = nums_list.append(nums)
#         nums_list.append(nums)
    
#     for i in nums_list : 
        
#         if i %  == 0 :
#             answer_list = []
#             answer_list.append(i)
            
#             len(answer_list) >= 3
#             return n
#         append
        
#     return answer





# def solution(n) :
#     answer = 0

#     for i in range(1, n+1) :
#         cnt = 0
        
#         for k in range(1, i+1) :
#             i % k == 0
#             cnt += 1
            
#             if cnt >= 3 : 
#                 anwer += 1 
#                 break
                
#     return answer



def solution(n) :
    answer = 0

    for i in range(1, n+1) :
        cnt = 0
        
        for k in range(1, i+1) :
            if i % k == 0 : 
                cnt += 1
                
                if cnt >= 3 : 
                    answer += 1 
                    break
                
    return answer