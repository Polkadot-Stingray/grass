from collections import deque
def solution(n, edge):
    answer = 0
    A=[[] for i in range(n+1)]
    
    for i in edge:
        A[i[0]].append(i[1])
        A[i[1]].append(i[0])
        
    visited=[0]*(n+1)
    
    queue=deque()
    queue.append(1)
    visited[1]=1
    
    while queue:
        now=queue.popleft()
        for i in A[now]:
            if not visited[i]:
                visited[i]=visited[now]+1
                queue.append(i)
                
    max_value = max(visited)
    answer = visited.count(max_value)
    return answer