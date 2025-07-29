# 희소 DP / 배낭 문제
def solution(info, n, m):
    dp = [{} for _ in range(len(info))]

    if n - info[0][0] > 0:
        dp[0][(n - info[0][0], m)] = info[0][0]
    if m - info[0][1] > 0:
        dp[0][(n, m - info[0][1])] = 0

    for i in range(1, len(info)):
        for (prev_n, prev_m), prev_A in dp[i-1].items():
            # A가 훔치는 경우
            if prev_n - info[i][0] > 0:
                new_state = (prev_n - info[i][0], prev_m)
                new_A = prev_A + info[i][0]
                if new_state not in dp[i] or dp[i][new_state] > new_A:
                    dp[i][new_state] = new_A
            
            # B가 훔치는 경우
            if prev_m - info[i][1] > 0:
                new_state = (prev_n, prev_m - info[i][1])
                new_A = prev_A
                if new_state not in dp[i] or dp[i][new_state] > new_A:
                    dp[i][new_state] = new_A
        
    if dp[-1]:
        return min(dp[-1].values())
    
    return -1

print(solution([[2,2],[2,2]], 4, 4))