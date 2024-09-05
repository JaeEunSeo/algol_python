# 적록색약

# dfs로 방문하며 구역 끝나면 cnt += 1
# 시작점 잡는 방법 : 순회하면서 unvisited일 경우 탐색 시작
import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [input() for i in range(N)]

def dfs(x,y, blind):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cur = graph[x][y]
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny]:
            if cur == graph[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny, blind)
            if blind and ((cur == 'R' and graph[nx][ny]=='G') or (cur == 'G' and graph[nx][ny]=='R')):
                visited[nx][ny] = True
                dfs(nx,ny, blind)
    return

cnt_a = 0; cnt_b = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j, False)
            cnt_a += 1

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j, True)
            cnt_b += 1

print(cnt_a, cnt_b)