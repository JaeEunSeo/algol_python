# 2차원 배열 dp 
# 첫번째 차원 : 자리 수
# 두번째 차원 : 마지막 숫자 : +1, -1

# 숫자로 접근할 것이 아니라 개수로 접근할 것. 내가 구해야 하는 것은 개수일 뿐이다.

N = int(input())
dp = [[0] * 10 for _ in range(N+1)]

for i in range(1,10):
    dp[1][i]=1

MOD = 1000000000

for i in range(2,N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N])%MOD)