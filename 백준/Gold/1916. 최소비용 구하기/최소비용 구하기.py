import heapq
import sys
input=sys.stdin.readline

N=int(input()) #노드개수
M=int(input()) #엣지개수
graph=[[] for _ in range(N+1)]

for _ in range(M):
    Data=list(map(int,input().split()))
    graph[Data[0]].append((Data[1],Data[2]))

start, end=map(int, input().split())

def dijkstra(graph, start):
    distances=[int(1e9)]*(N+1)
    distances[start]=0
    queue=[]
    heapq.heappush(queue, [distances[start], start])

    while queue:
        dist, node=heapq.heappop(queue)

        if distances[node]<dist:
            continue

        for next_node, next_dist in graph[node]:
            distance=dist+next_dist
            if distance < distances[next_node]:
                distances[next_node]=distance
                heapq.heappush(queue, [distance, next_node])

    return distances

dist_start=dijkstra(graph,start)
print(dist_start[end])