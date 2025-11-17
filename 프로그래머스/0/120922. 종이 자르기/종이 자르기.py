def solution(M, N):
    # M x N개의 1x1 조각을 만들려면 총 조각 수가 M*N개가 되어야 한다.
    # 처음 종이는 1조각이므로, 조각 수를 (M*N)까지 늘리려면 (M*N - 1)번 잘라야 한다.
    answer = M * N - 1
    
    return answer