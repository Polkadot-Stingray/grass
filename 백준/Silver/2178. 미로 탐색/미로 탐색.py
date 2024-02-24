import sys
input=sys.stdin.readline

from collections import deque
dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
N, M=map(int, input().split())
grid=[[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

for i in range(N):
    num=list(input())
    for j in range(M):
        grid[i][j]=int(num[j])

def bfs(i, j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    while queue:
        now=queue.popleft()
        for k in range(4):
            x=now[0]+dx[k]
            y=now[1]+dy[k]
            if x>=0 and y>=0 and x<N and y<M:
                if grid[x][y]!=0 and not visited[x][y]:
                    visited[x][y]=True
                    grid[x][y]=grid[now[0]][now[1]]+1
                    queue.append((x,y))

bfs(0,0)
print(grid[N-1][M-1])