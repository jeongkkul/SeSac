# # 첫 코드
# # n을 array 한 요소마다 다 뺀다음 차이의 절대값이 가장 작은 요소를 추출하면 어떨까
# # 뺀 요소들을 다시 리스트에 집어넣고 min함수 이용할까

# def solution(array, n):
#     answer = 0
    
#     list1 = []
    
#     for i in range(1, len(array)+1) :
#         list1 = n - array[i]
        
#     abs(min(list1))
    
    
#     return answer


def solution(array, n):
    # 1️⃣ 각 원소와 n의 차이(거리)를 계산해서 리스트로 저장
    differences = [abs(num - n) for num in array]

    # 2️⃣ 차이 중에서 가장 작은 값(가장 가까운 거리)을 찾기
    min_diff = min(differences)

    # 3️⃣ 그 최소 거리와 같은 원소들만 추려내기
    nearest_numbers = []
    for i in range(len(array)):
        if differences[i] == min_diff:
            nearest_numbers.append(array[i])

    # 4️⃣ 여러 개면 더 작은 수를 반환
    answer = min(nearest_numbers)
    return answer
