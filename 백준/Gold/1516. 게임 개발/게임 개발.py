from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
A=[[] for i in range(N+1)]
indegree=[0]*(N+1)
building=[0]*(N+1)
for i in range(1, N+1):
    temp=list(map(int,input().split()))
    building[i]=temp.pop(0)
    for j in temp:
        if j==-1:
            break
        A[j].append(i)
        indegree[i]+=1
queue=deque()
for i in range(1, N+1):
    if indegree[i]==0:
        queue.append(i)

result=[0]*(N+1)

while queue:
    now=queue.popleft()
    for next in A[now]:
        indegree[next]-=1
        result[next]=max(result[next], result[now]+building[now])
        if indegree[next]==0:
            queue.append(next)

for i in range(1, N+1):
    print(result[i] + building[i])