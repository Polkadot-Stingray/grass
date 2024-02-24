import sys
input=sys.stdin.readline

N, M=map(int, input().split())
array=list(map(int, input().split()))
sumar=[0]*N
sumar[0]=array[0]
index=[0]*M
answer=0

for i in range(1, N):
    sumar[i]=sumar[i-1]+array[i]

for i in range(N):
    temp=sumar[i]%M
    if temp==0:
        answer+=1
    index[temp]+=1

for i in range(M):
    if index[i]>1:
        answer += (index[i]*(index[i]-1)//2)

print(answer)
#혼자 나중에 풀어