# # 첫 코드 

# # 1. 한 번만 등장한 문자=one 들 우선 뽑기
# # 2. one을 사전순으로 정렬(오름차순으로 정렬) 해서 return

# def solution(s):
#     answer = ''
    
#     text1 = s
#     text_list = list(text1)
    
#     for i in text_list:
#         cnt = 0
#         cnt += 1
#         for k in text_list[]
    
#     return answer


def solution(s):
    answer = ''
    for ch in sorted(s):           # 사전순 정렬
        if s.count(ch) == 1:       # 한 번만 등장하는 문자만
            answer += ch
    return answer
