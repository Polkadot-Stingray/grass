import sys
input=sys.stdin.readline

N=int(input())
a=[]
for i in range(N):
	temp=list(map(int, input().split()))
	a.append(temp)

for i in range(1, N):
	for j in range(i+1):
		if j==0:
			a[i][j]+=a[i-1][j]
		elif j==i:
			a[i][j]+=a[i-1][j-1]
		else:
			a[i][j]+=max(a[i-1][j-1], a[i-1][j])

print(max(a[N-1]))