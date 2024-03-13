from collections import deque
def solution(maps):
    answer = 0
    row=len(maps)
    column=len(maps[0])
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    visited=[[False] * column for i in range(row)]
    queue=deque()
    queue.append((0,0))
    visited[0][0]=True
    while queue:
        now=queue.popleft()
        for i in range(4):
            sero=now[0]+dy[i]
            garo=now[1]+dx[i]
            if garo>=0 and garo<column and sero>=0 and sero<row and maps[sero][garo]!=0 and not visited[sero][garo]:
                maps[sero][garo]=maps[now[0]][now[1]]+1
                visited[sero][garo]=True
                queue.append((sero, garo))

    if maps[row-1][column-1]==1:
        return -1
    
                
    return maps[row-1][column-1]