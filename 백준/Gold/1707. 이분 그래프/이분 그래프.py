import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
K=int(input())
IsEven=True

def DFS(start):
    global IsEven
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            check[i]=(check[start]+1)%2
            DFS(i)
        elif check[start]==check[i]:
            IsEven=False
            
for _ in range(K):
    V, E=map(int, input().split())
    graph=[[] for _ in range(V+1)]
    visited=[False]*(V+1)
    check=[0]*(V+1)
    IsEven=True
    
    for i in range(E):
        a, b=map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, V+1):
        if IsEven:
            DFS(i)
        else:
            break
    
    if IsEven:
        print("YES")
        
    else:
        print("NO")