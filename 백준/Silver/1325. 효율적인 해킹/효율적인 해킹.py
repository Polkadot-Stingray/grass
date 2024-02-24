import sys
input=sys.stdin.readline
from collections import deque
N,M=map(int, input().split())
grid=[[] for _ in range(N+1)]

def bfs(v):
    cnt=1
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        now=queue.popleft()
        for i in grid[now]:
            if not visited[i]:
                visited[i]=True
                cnt+=1
                queue.append(i)
    return cnt

for _ in range(M):
    x,y=map(int, input().split())
    grid[y].append(x)


maxCnt=1
ans=[]

for i in range(1, N+1):
    visited=[False]*(N+1)
    cnt=bfs(i)
    if cnt>maxCnt:
        maxCnt=cnt
        ans.clear()
        ans.append(i)
    elif cnt==maxCnt:
        ans.append(i)

print(*ans)