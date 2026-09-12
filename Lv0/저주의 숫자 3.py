# https://school.programmers.co.kr/learn/courses/30/lessons/120871
def solution(n):
    # 일단 3의 배수 제거한 리스트 생성
    new_num = [str(i) for i in range(1,250) if (i%3) != 0]
    # 3이 들어가 있는 수 제거한 리스트 생성
    fin_num =[int(i) for i in new_num if i.find('3') == -1]
    print(fin_num)
    #리스트 출력
    return fin_num[n-1]
        
    
