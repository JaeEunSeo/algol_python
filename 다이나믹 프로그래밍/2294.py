from itertools import combinations
n, k = map(int, input().split())
coins = set()
for _ in range(n):
    c = int(input())
    coins.add(c)
dp = [[10001] for _ in range(k+1)]
dp[0][0] = 0

for c in coins:
    for i in range(k+1):
        if i>=c:
            dp[i][0] = min(dp[i][0], dp[i-c][0]+1)

if dp[k][0] == 10001:
    print("-1")
else:
    print(dp[k][0])
        
