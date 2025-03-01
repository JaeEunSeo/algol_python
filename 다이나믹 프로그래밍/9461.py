# 파도반 수열
n = int(input())

def dp(n):
    if n <= 3:
        return 1
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n):
        dp[i] = dp[i-2]+dp[i-3]
    return dp[n-1]

for _ in range(n):
    k = int(input())
    print(dp(k))