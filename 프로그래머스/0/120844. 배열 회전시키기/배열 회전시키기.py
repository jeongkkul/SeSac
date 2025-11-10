def solution(numbers, direction):
    # ① 길이 제한 확인
    if not (3 <= len(numbers) <= 20):
        return numbers  # 조건에 맞지 않으면 원본 그대로 반환
    
    # ② 방향 제한 확인
    if direction not in ["left", "right"]:
        return numbers  # 잘못된 입력일 경우 원본 반환

    # ③ 복사본 생성
    nums = numbers[:]

    # ④ 회전 로직
    if direction == "right":
        nums.insert(0, nums[-1])
        nums.pop()
    else:
        nums.append(nums[0])
        nums.pop(0)

    return nums