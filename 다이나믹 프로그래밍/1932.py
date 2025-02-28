n = int(input())
triangle = []
for i in range(n):
    layer = list(map(int, input().split()))
    triangle.append(layer)

# dp 테이블 초기화 방식 유의하기
dp = [[0] * _ for _ in range(1,n+1)]
dp[0] = triangle[0]

if n > 1:
    dp[1] = [dp[0][0]+triangle[1][0], dp[0][0]+triangle[1][1]]
for i in range(2, n):
    layer = []
    dp[i][0] = dp[i-1][0]+triangle[i][0]
    dp[i][i] = dp[i-1][i-1]+triangle[i][i]
    for j in range(1,i):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+triangle[i][j]

print(max(dp[-1]))