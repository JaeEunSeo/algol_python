    if dp[i][j] == float('inf'):
                        continue
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1