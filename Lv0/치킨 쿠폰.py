# https://school.programmers.co.kr/learn/courses/30/lessons/120884
def solution(chicken):
    coupon = chicken
    result = 0
    if coupon < 10: return 0
    while(coupon >= 10):
        service_ch = 0
        service_ch += coupon//10
        coupon = coupon - coupon//10*10 + service_ch
        result += service_ch
    return result
