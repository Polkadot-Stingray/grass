import math
Min=int(input())

A=[0]*10000001

for i in range(2, 10000001):
    A[i]=i

for i in range(2, 10000001):
    if A[i]==0:
        continue
    for j in range(i+i, 10000001, i):
        A[j]=0

def isPelindrome(target):
    temp=list(str(target))
    s=0
    e=len(temp)-1
    while s<e:
        if temp[s]!=temp[e]:
            return False
        s+=1
        e-=1
    return True

i=Min

while True:
    if A[i]!=0:
        result=A[i]
        if (isPelindrome(result)):
            print(result)
            break
    i+=1