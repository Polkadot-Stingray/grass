def solution(want, number, discount):
    answer = 0
    length=len(discount)
    for i in range(length):
        count=[0]*len(want)
        can=True
        if i+10>length:
            for j in range(i, length):
                if discount[j] in want:
                    count[want.index(discount[j])]+=1
            for j in range(len(want)):
                if count[j]<number[j]:
                    can=False
        else:
            for j in range(i, i+10):
                if discount[j] in want:
                    count[want.index(discount[j])]+=1
            for j in range(len(want)):
                if count[j]<number[j]:
                    can=False   
        
        if can:
            answer+=1
    return answer