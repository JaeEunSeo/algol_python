N, X = map(int, input().split())
visit = list(map(int, input().split()))
# 누적합
prefix = [0] * (N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + visit[i]

max_answer = 0
cnt = 1
for i in range(X, N+1):
    if (max_answer == prefix[i]-prefix[i-X]):
        cnt += 1
    elif (max_answer < prefix[i]-prefix[i-X]):
        max_answer = max(max_answer, prefix[i] - prefix[i-X])
        cnt = 1

if (max_answer > 0):
    print(max_answer)
    print(cnt)
else:
    print("SAD")