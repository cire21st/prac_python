# https://school.programmers.co.kr/learn/courses/30/lessons/120882
def solution(score):
    avg_score, val_list = [],[]
    
    for i,s in enumerate(score):
        avg_score.append(sum(s)) #평균을 원소로 갖는 list 생성
        val_list.append(i+1) #1,2,3...n으로 초기화된 list 생성
    
    #오리지널 스코어 백업
    orgin_score = avg_score[:]
    # 스코어 리스트를 sorting한후 순위를 매기고 key list로 만들기 ex. [100, 130, 150] 
    avg_score.sort(reverse = True) #score list = key list
    for i in range(len(avg_score)): 
        if (i < len(avg_score) - 1) and avg_score[i] == avg_score[i+1]:
            val_list[i+1] = val_list[i] 
    #zip(key,value)로 디셔너리로 만들고 원래 스코어리스트에 있는 값을 바탕으로 순위 값으로 변환, 이를 return
    answer_list = dict(zip(avg_score,val_list))
    return [answer_list.get(i) for i in orgin_score]
