def solution(priorities, location):
    answer = 1
    length=len(priorities)
    alpha=[]
    for i in range(length):
        alpha.append(chr(ord('A')+i))
    char=chr(ord('A')+location)
    while alpha:
        if priorities[0]==max(priorities):
            if alpha[0]==char:
                break
            priorities.pop(0)
            alpha.pop(0)
            answer+=1
        else:
            priorities.append(priorities.pop(0))
            alpha.append(alpha.pop(0))
    return answer