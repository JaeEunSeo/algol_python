'''
프로그래머스 : lv3
정수 삼각형
'''

def solution(triangle):
    answer = 0
    dp = [[0] * (i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == int(len(triangle[i])-1):
                dp[i][j] = dp[i-1][-1] + triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
    answer = max(map(max, dp))
    return answer