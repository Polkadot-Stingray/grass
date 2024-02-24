import sys
input=sys.stdin.readline

N, M=map(int, input().split())
a=list(map(int, input().split()))

a.sort()
start, end=1, max(a)

while start<=end:
    mid=(start+end)//2
    miter=0
    for i in a:
        if i>=mid:
            miter+=i-mid
            
    if miter>=M:
        start=mid+1
    else:
        end=mid-1
print(end)