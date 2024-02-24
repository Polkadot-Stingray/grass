import sys
input=sys.stdin.readline
from collections import deque

N,M,K,X=map(int,input().split())
graph=[[] for i in range(N+1)]
visited=[-1]*(N+1)
ans=[]

for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)

def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v]+=1
    while queue:
        now=queue.popleft()
        for i in graph[now]:
            if visited[i]==-1:
                visited[i]=visited[now]+1
                queue.append(i)

BFS(X)

for i in range(N+1):
    if visited[i]==K:
        ans.append(i)

if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)