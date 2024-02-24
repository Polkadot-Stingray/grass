import sys
sys.setrecursionlimit(10**6)
from collections import deque

n,m,start=map(int, input().split())
A=[[] for i in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    a,b=map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for i in range(n+1):
    A[i].sort()
def DFS(v):
    visited[v]=True
    print(v, end=" ")

    for i in A[v]:
        if not visited[i]:
            DFS(i)

DFS(start)

def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v]=True

    while queue:
        now=queue.popleft()
        print(now, end=" ")
        for i in A[now]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

visited=[False]*(n+1)
print()
BFS(start)
