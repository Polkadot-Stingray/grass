
N=int(input())
a=list(map(int, input().split()))
M=int(input())
b=list(map(int, input().split()))
a.sort()
for i in b:
    check=0
    start=0
    end=len(a)-1
    while True:
        mid=(start+end)//2
        if i==a[mid]:
            check=1
            break
        elif start>=end:
            break
        elif i<a[mid]:
            end=mid-1
        else:
            start=mid+1
    print(check)
