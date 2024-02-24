import sys
input=sys.stdin.readline

least=[0]*4
a=[0]*4
count=0

def new(c):
    global least, a, count
    if c=='A':
        a[0]+=1
        if a[0]==least[0]:
            count+=1
    elif c=='C':
        a[1]+=1
        if a[1]==least[1]:
            count+=1
    elif c=='G':
        a[2]+=1
        if a[2]==least[2]:
            count+=1
    elif c=='T':
        a[3]+=1
        if a[3]==least[3]:
            count+=1

def erase(c):
    global least, a, count
    if c=='A':
        if a[0]==least[0]:
            count-=1
        a[0]-=1
    elif c=='C':
        if a[1]==least[1]:
            count-=1
        a[1]-=1
    elif c=='G':
        if a[2]==least[2]:
            count-=1
        a[2]-=1
    elif c=='T':
        if a[3]==least[3]:
            count-=1
        a[3]-=1

s,p=map(int, input().split())
dna=list(input())
ans=0
least=list(map(int, input().split()))

for i in range(4):
    if least[i]==0:
        count+=1

for i in range(p):
    new(dna[i])

if count==4:
    ans+=1

for i in range(p,s):
    j=i-p
    new(dna[i])
    erase(dna[j])
    if count==4:
        ans+=1

print(ans)