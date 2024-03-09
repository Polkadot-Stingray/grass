from collections import deque

def solution(n, computers):
    answer = 0
    A=[[] for _ in range(n)]
    visited=[False]*n
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and i!=j:
                A[i].append(j)
                
    def BFS(v):
        queue=deque()
        visited[v]=True
        queue.append(v)
    
        while queue:
            now=queue.popleft()
            for i in A[now]:
                if not visited[i]:
                    visited[i]=True
                    queue.append(i)
                
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer+=1
            
    return answer


                