def solution(maps):
    cands = []
    n,m = len(maps), len(maps[0])
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    visited = [[False] * m for _ in range(n)]

    def dfs(y, x, length):
        if y == n-1 and x == m-1:
            cands.append(length)
            return
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if not visited[ny][nx] and maps[ny][nx]:
                    visited[ny][nx] = True
                    dfs(ny,nx,length+1)
                    visited[ny][nx] = False
                    
    visited[0][0] = True
    dfs(0,0,1)
    answer = min(cands) if answer else -1
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))