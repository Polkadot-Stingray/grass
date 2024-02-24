import sys
input=sys.stdin.readline

n=int(input())
array=list(map(int, input().split()))
count=0
array.sort()
for i in range(n):
    sindex=0
    eindex=n-1
    while sindex<eindex:
        if array[sindex]+array[eindex]==array[i]:
            if i!=sindex and i!=eindex:
                count+=1
                break
            elif i==sindex:
                sindex+=1
            else:
                eindex-=1
        elif array[sindex]+array[eindex]<array[i]:
            sindex+=1
        else:
            eindex-=1


print(count)