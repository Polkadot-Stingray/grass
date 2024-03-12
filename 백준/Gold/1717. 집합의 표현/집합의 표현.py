import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
A=[]
n, m=map(int, input().split())

for i in range(n+1):
    A.append(i)

def find(num):
    if A[num]==num:
        return num
    else:
        A[num]=find(A[num])
        return A[num]

def union(a, b):
    a=find(a)
    b=find(b)
    if a!=b:
        A[b]=a

def checksame(a, b):
    a=find(a)
    b=find(b)
    if a!=b:
        return False
    else:
        return True

for i in range(m):
    num, a, b=map(int, input().split())
    if num==0:
        union(a, b)
    else:
        if checksame(a, b):
            print("YES")
        else:
            print("NO")