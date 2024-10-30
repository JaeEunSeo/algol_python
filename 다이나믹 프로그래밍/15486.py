'''
백준 : 골드5
퇴사 2
'''
import sys
input = sys.stdin.readline

N = int(input())
t, p = [0 for _ in range(N + 1)], [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    t[i], p[i] = map(int, input().split())
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    dp[i] = max(dp[i], dp[i-1])
    end = i + t[i] - 1
    if end > N :
        continue
    dp[end] = max(dp[end], dp[i-1] + p[i])

print(max(dp))