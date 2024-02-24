import math

minimal, maximum=map(int, input().split())
A=[False]*(maximum-minimal+1)

for i in range(2, int(math.sqrt(maximum))+1):
    pow=i*i
    start_index=int(minimal/pow)
    if minimal%pow!=0:
        start_index+=1
    for j in range(start_index, int(maximum/pow)+1):
        A[j*pow-minimal]=True

count=0

for i in range(0, maximum-minimal+1):
    if A[i]==False:
        count+=1

print(count)