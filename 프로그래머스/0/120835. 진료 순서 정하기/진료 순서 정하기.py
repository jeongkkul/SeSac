# # 내 코드
# # 정수 배열 emergency
# # 먼저 응급도를 다 구한 다음 순서를 각 인덱스에 집어넣기?
# # sort_value()를 이용해서 내림차순으로 정렬 후 rank = [76, 24, 3]
# # = rank[0] 
# # 
# # 76 = rank[0] = 1 ( len(score) =energency(1)
# #  24 = rank[1] = 2 (len(score)) = emergency(2)
# # 3 = rank[2] = 3 len(score) = emergency(0)

# def solution(emergency):
#     answer = []
    
#     rank = emergency.sort_value()
#     rank[i]
    
#     return answer




def solution(emergency):
    # 큰 값일수록 높은 우선순위 → 내림차순
    desc = sorted(emergency, reverse=True)          # 예: [3, 76, 24] → [76, 24, 3]
    rank = {desc[i]: i + 1 for i in range(len(desc))}  # {76:1, 24:2, 3:3}
    return [rank[x] for x in emergency]

    