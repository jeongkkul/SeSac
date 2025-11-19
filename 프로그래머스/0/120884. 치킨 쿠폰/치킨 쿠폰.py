def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        service = coupon // 10      # 서비스 치킨 수
        answer += service           # 서비스 치킨 누적
        coupon = service + (coupon % 10)   # 새 쿠폰 + 남은 쿠폰

    return answer
