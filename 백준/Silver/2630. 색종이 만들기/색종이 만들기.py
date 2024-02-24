import sys
input=sys.stdin.readline

result=[]
def cut(start, end, N):
    first=ar[start][end]
    for i in range(start, start+N):
        for j in range(end, end+N):
            if ar[i][j]!=first:
                cut(start, end, N//2)
                cut(start, end+N//2, N//2)
                cut(start+N//2, end, N//2)
                cut(start+N//2, end+N//2, N//2)
                return
    if first==0:
        result.append(0)
    else:
        result.append(1)


N=int(input())
ar=[]
for i in range(N):
    temp=list(map(int, input().split()))
    ar.append(temp)

cut(0, 0, N)
print(result.count(0))
print(result.count(1))