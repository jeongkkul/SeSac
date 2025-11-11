def solution(before, after):
    # 두 문자열의 문자를 정렬해서 비교
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0