# https://school.programmers.co.kr/learn/courses/30/lessons/120882
import copy

def solution(score):
    for i in range(len(score)):
    avg_score = (score[i][0] + score[i][1])/2
    
    def ranking(score_list):
        # 원래 스코어 리스트를 따로 저장 [150, 100, 130]
        orgin_score = copy.deepcopy(score_list)
        # 스코어 리스트를 sorting한후 순위를 매기고 value list로 만들기 [100, 130, 150] 
        score_list.sort() #score list = value list
        #같은 값이면 몇명인지에 따라 공동순위 설정하고 이를 key list로 만들기
        key_list = []
        tie = 0
        for i in range(len(score_list)): 
            if score_list[i] == score_list[i+1]:
                tie = tie + 1
                key_list[i] = i + 1
                key_list[i+1] = i + 1
                #tie의 수를 저장해놨다가 그거만큼 더해서 순위를 띄워주고 tie는 그럴떄마다 다시 초기화
        #zip(key,value)로 디셔너리로 만들고 원래 스코어리스트에 있는 값을 바탕으로 순위 값으로 변환, 이를 return
        
    
