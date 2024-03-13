N=int(input())
M=int(input())
parent=[0]*(N+1)

for i in range(N+1):
    parent[i]=i
def find(num):
    if num==parent[num]:
        return num
    else:
        return find(parent[num])

def union(a, b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a

def checksame(a, b):
    a=find(a)
    b=find(b)
    if a==b:
        return True
    return False

for i in range(N):
    temp=list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j]==1:
            union(i+1, j+1)

problem=list(map(int, input().split()))
is_connected=True
first=problem[0]
for i in problem:
    if not checksame(first, i):
        is_connected=False

if is_connected:
    print("YES")
else:
    print("NO")
