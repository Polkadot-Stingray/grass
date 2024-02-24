def solution(cards):
    answer = 0
    n=len(cards)
    graph=[[] for _ in range(n+1)]
    for i in range(n):
        graph[i+1].append(cards[i])


    def DFS(v, depth):
        visited[v]=True
        if visited[graph[v][0]]:
            return depth
        else:
            return DFS(graph[v][0], depth+1)

    de=[]
    for i in range(n):
        visited=[False]*(n+1)
        dep=DFS(i+1, 1)
        print(visited)
        alltrue=True
        for i in range(1, n+1):
            if visited[i]==False:
                alltrue=False
        de.append(dep)
    if alltrue:
        return 0
    de=list(set(de))
    de.sort()
    if len(de)==1:
        answer=de[0]*de[0]
    else:    
        fir=de.pop()
        se=de.pop()
        answer=fir*se
        
    return answer