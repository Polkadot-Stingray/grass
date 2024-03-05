from collections import deque

N=int(input())
A=[[] for _ in range(N+1)]

for i in range(N-1):
    a, b, c=map(int,input().split())
    A[a].append((b,c))
    A[b].append((a,c))

visited=[False]*(N+1)
distance=[0]*(N+1)

def BFS(v):
    queue=deque()
    visited[v]=True

    queue.append(v)
    while queue:
        now=queue.popleft()
        for i in A[now]:
            if not visited[i[0]]:
                visited[i[0]]=True
                distance[i[0]]=distance[now]+i[1]
                queue.append(i[0])

BFS(1)
MAX=1
for i in range(2, N+1):
    if distance[MAX]<distance[i]:
        MAX=i

distance=[0]*(N+1)
visited=[False]*(N+1)

BFS(MAX)
distance.sort()
print(distance[N])