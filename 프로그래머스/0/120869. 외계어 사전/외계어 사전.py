def solution(spell, dic):
    answer = 2  # 기본값: 조건에 맞는 단어가 없다고 가정

    for word in dic:
        # 1. 길이가 다르면 spell의 글자를 모두 쓸 수 없으므로 패스
        if len(word) != len(spell):
            continue

        # 2. spell의 문자 각각이 word 안에 정확히 1번씩 있는지 검사
        is_valid = True
        for ch in spell:
            if word.count(ch) != 1:
                is_valid = False
                break

        # 3. 모든 조건 만족 → answer를 1로 바꾸고 반복 종료
        if is_valid:
            answer = 1
            break

    return answer