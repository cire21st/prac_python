#https://school.programmers.co.kr/learn/courses/30/lessons/120804
def solution (num1: int, num2: int) -> int:
    if (0 <= num1 <= 100) and (0 <= num2 <= 100):
        return num1 * num2
    else:
        return 0
