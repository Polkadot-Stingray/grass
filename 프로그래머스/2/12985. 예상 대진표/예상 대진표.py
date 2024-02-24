def solution(n,a,b):
    answer = 1

    if a<b:
        while True:
            if a%2==1 and b==a+1:
                break
            if a%2==1:
                a+=1
            if b%2==1:
                b+=1
            a=a//2
            b=b//2
            answer+=1
    else:
        while True:
            if b%2==1 and a==b+1:
                break
            if a%2==1:
                a+=1
            if b%2==1:
                b+=1
            a=a//2
            b=b//2
            answer+=1
            
    return answer