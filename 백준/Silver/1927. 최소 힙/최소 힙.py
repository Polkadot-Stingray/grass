import sys
input=sys.stdin.readline

import heapq

n=int(input())
array=[]
for _ in range(n):
    temp=int(input())
    if temp!=0:
        heapq.heappush(array, temp)
    else:
        try:
            print(heapq.heappop(array))
        except:
            print(0)