def solution(n, s):
    answer = []
    if n>s:
        return [-1]
    quotient=s//n
    rest=s%n
    
    for _ in range(n):
        answer.append(quotient)
    i=0
    while rest>0:
        answer[i]+=1
        rest-=1
        i+=1
        if i>n:
            i=0
    answer.sort()
    return answer