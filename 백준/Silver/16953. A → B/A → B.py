import sys
input=sys.stdin.readline

cnt=1
A, B=map(int, input().split())
while A!=B:
    if (B%10!=1 and B%2!=0) or (B<A):
        cnt=-1
        break
    elif B%10==1:
        B=B//10
        cnt+=1
    elif B%2==0:
        B=B//2
        cnt+=1

print(cnt)