import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n=int(input())

def is_prime(n):
    for i in range(2, int(n/2+1)):
        if n%i==0:
            return False
    return True

def dfs(num):
    if len(str(num))==n:
        print(num)
    else:
        for i in range(1, 10):
            if i%2==0:
                continue
            if is_prime(num*10+i):
                dfs(num*10+i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)