# https://school.programmers.co.kr/learn/courses/30/lessons/120861
def solution(keyinput, board):
    x_lim, y_lim = board[0]//2, board[1]//2
    
    move = {'left': (-1,0), 'right': (1,0), 'up': (0, 1), 'down': (0, -1)}
    x, y = 0, 0
    for key in keyinput:
        add_x, add_y = move[key]
        
        if abs(x + add_x) > x_lim or abs(y + add_y) > y_lim:
            continue
        else: 
            x +=add_x 
            y +=add_y
    
    return [x,y]
        
