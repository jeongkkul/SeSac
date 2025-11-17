def solution(keyinput, board):
    answer = [0, 0]  # 기본 좌표는 [0, 0]으로 시작

    # x, y 좌표를 따로 관리
    x = 0
    y = 0

    # 이동 가능한 최대/최소 좌표 계산
    max_x = board[0] // 2  # 가로 방향 최대
    min_x = -max_x         # 가로 방향 최소
    max_y = board[1] // 2  # 세로 방향 최대
    min_y = -max_y         # 세로 방향 최소

    # keyinput에 들어있는 방향을 하나씩 처리
    for key in keyinput:
        if key == "up":
            # 위로 한 칸 가도 범위 안이면 이동
            if y + 1 <= max_y:
                y += 1
        elif key == "down":
            if y - 1 >= min_y:
                y -= 1
        elif key == "left":
            if x - 1 >= min_x:
                x -= 1
        elif key == "right":
            if x + 1 <= max_x:
                x += 1

    # 마지막 위치를 answer에 담기
    answer = [x, y]
    return answer