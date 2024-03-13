n, m=map(int, input().split())
know=list(map(int, input().split()))
know.pop(0)
parent=[0]*(n+1)
count=0
for i in range(n+1):
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

party=[]
for i in range(m): #여기에선 미리 union 작업해두기
    temp=list(map(int, input().split()))
    temp.pop(0)
    party.append(temp)
    first=temp[0]
    for j in temp:
        union(first, j)

for i in range(m): #가능한지 여부확인하기
    is_possible=True
    first=party[i][0]
    for j in know:
        if find(first)==find(j):
            is_possible=False
            break
    if is_possible:
        count+=1
        
print(count)