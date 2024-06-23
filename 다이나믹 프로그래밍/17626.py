#DP
n = int(input())
dp = [0,1]

for i in range(2, n+1):
    tmp = []
    j = 1
    while (j**2) <=i:
        tmp.append(min(dp[i-j**2], 4)+1)
        j += 1
    dp.append(min(tmp))

print(dp[n])