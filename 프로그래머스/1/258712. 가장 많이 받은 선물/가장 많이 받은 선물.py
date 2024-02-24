def solution(friends, gifts):
    answer = 0
    length=len(friends)
    score=[0]*length
    
    #0 
    present=[[0]*length for _ in range(length)]
    for i in gifts:
        gift=i.split(" ")
        giver=friends.index(gift[0])
        given=friends.index(gift[1])
        
        present[giver][given]+=1
        
    for i in range(length):
        for j in range(i + 1, length):    
            give_score = present[i][j] # i가 j에게 준 선물의 개수
            get_score = present[j][i] #j가 i에게 준 선물의 개수
            
            if (give_score != get_score) and (give_score > 0 or get_score > 0):
                if give_score > get_score:
                    score[i] += 1

                else:
                    score[j] += 1
                    
            #1-2. 선물 지수 계산
            else:
                giver_present_score = sum(present[i])
                getter_present_score = sum(present[j])

                for k in range(length):
                    giver_present_score -= present[k][i]
                    getter_present_score -= present[k][j]


                if giver_present_score > getter_present_score:
                    score[i] += 1

                elif giver_present_score < getter_present_score:
                    score[j] += 1
        
    answer=max(score)    
    return answer