# # 첫 코드
# # 나누기 split
# # 각 길이 재기 len

# def solution(myString):
#     answer = []
    
#     str1 = mystring.split('x')
#     len1 = len(str1)
    
    
#     return answer

def solution(myString):
    
    parts = myString.split('x')
    return [len(p) for p in parts]