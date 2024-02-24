import sys
input=sys.stdin.readline

N, M=map(int, input().split())

array=list(map(int, input().split()))
sumarray=[0]
temp=0
for i in range(N):
    temp+=array[i]
    sumarray.append(temp)

for _ in range(M):
    start, end=map(int, input().split())
    print(sumarray[end]-sumarray[start-1])