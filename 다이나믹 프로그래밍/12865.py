# DP 문제 중에서도 W, V와 같이 고려해야하는 변수가 두가지인 경우 - 2차원 배열로 처리
N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
weights = [0]
values = [0]

for i in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)


for i in range(1,N+1):
    for j in range(1,K+1):
        if j < weights[i] :
           # K는 담을 수 있는 최대 무게, j가 해당 물건 무게보다 작다 -> 물건을 담을 수 없음
           # dp 값에는 이전 회차의 값이 그대로 들어감
           dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
        
print(dp[N][K])