from collections import deque
def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    values = [0] * m
    visited = [[False]*m for _ in range(n)]
    
    dx, dy = [-1,1,0,0],[0,0,-1,1]

    # BFS -> 석유의 개수와 존재하는 열을 파악한다.
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]==1:
                # 하나 시작.
                count, cols = 0, set()
                queue = deque([[i,j]])
                visited[i][j] = True

                while queue:
                    x,y = queue.popleft()
                    count += 1
                    cols.add(y)

                    for _ in range(4):
                        nx, ny = x+dx[_], y+dy[_]
                        if (0<=nx<n) and (0<=ny<m) and (not visited[nx][ny]) and (land[nx][ny]==1):
                            queue.append([nx,ny])
                            visited[nx][ny] = True

                for col in cols:
                    values[col] += count
    answer = max(values)
    return answer