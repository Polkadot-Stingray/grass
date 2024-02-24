def solution(k, m, score):
    answer = 0
    many=len(score)
    score.sort()
    
    for _ in range(many//m):
        box=[]
        for _ in range(m):
            box.append(score.pop())
        sc=min(box)
        answer+=sc*m
        
    
    return answer