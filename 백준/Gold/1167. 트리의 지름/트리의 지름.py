import sys
input=sys.stdin.readline

from collections import deque

V=int(input())
Grid=[[] for _ in range(V+1)]

for i in range(V):
    Data=list(map(int, input().split()))
    index=0
    Node=Data[index]
    index=+1
    while True:
        E=Data[index]
        if E==-1:
            break
        val=Data[index+1]
        Grid[Node].append((E,val))
        index+=2

dis=[0]*(V+1)
visited=[False]*(V+1)

def BFS(node):
    queue=deque()
    queue.append(node)
    visited[node]=True
    while queue:
        cur=queue.popleft()
        for i in Grid[cur]:
            if not visited[i[0]]:
                visited[i[0]]=True
                queue.append(i[0])
                dis[i[0]]=dis[cur]+i[1]

BFS(1)
Max=1
for i in range(2, V+1):
    if dis[Max]<dis[i]:
        Max=i

dis=[0]*(V+1)
visited=[False]*(V+1)
BFS(Max)
dis.sort()
print(dis[V])