import sys
input=sys.stdin.readline

K, N=map(int, input().split())
lis=[]
for _ in range(K):
    lis.append(int(input()))
start, end=1, max(lis)

while start<=end:
    mid=(start+end)//2
    lines=0
    for i in lis:
        lines+=i//mid
    if lines>=N:
        start=mid+1
    else:
        end=mid-1
print(end)
