# BFS - 유기농 배추
from collections import deque

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    graph[i][j] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<N) and (0<=ny<M):
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0


for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    cnt = 0
    for j in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    # 여기서 BFS 호출
    print(cnt)
