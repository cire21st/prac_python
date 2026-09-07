# https://school.programmers.co.kr/learn/courses/30/lessons/120883?language=python3
def solution(id_pw, db):
    if dict(db).get(id_pw[0]) == id_pw[1]: return "login"
    elif dict(db).get(id_pw[0]): return "wrong pw"
    else: return "fail"
