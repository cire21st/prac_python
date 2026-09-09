# https://school.programmers.co.kr/learn/courses/30/lessons/120860
def solution(dots):
    x_list, y_list = map(list,zip(*dots))
    return (max(x_list)-min(x_list)) * (max(y_list)-min(y_list)) 
