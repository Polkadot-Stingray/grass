dp=[0]*((10**6)+1)
dp[1]=0
for i in range(2, 10**6+1):
    if i%6==0:
        dp[i]=min(dp[i//2], dp[i//3])+1

    elif i%3==0:
        dp[i]=min(dp[i//3], dp[i-1]) + 1

    elif i%2==0:
        dp[i]=min(dp[i//2], dp[i-1])+1

    else:
        dp[i]=dp[i-1]+1

N=int(input())
print(dp[N])