# 알고스팟
from collections import deque
M, N = map(int, input().split())

maze = [input().split()[0] for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 벽을 부수는 비용 - 최소값으로 갱신한다.
cost = int(1e4)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# x, y, 비용을 큐에 저장한다.
queue = deque([(0,0,0)])

while queue:
    cx, cy, sum = queue.popleft()
    visited[cx][cy] = True
    if (cx == N-1) and (cy == M-1):
        print(sum)
        break
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if not((0<=nx) and (nx<N) and (0<=ny) and (ny<M)):
            continue
        if visited[nx][ny]:
            continue
        if maze[nx][ny] == '1':
            queue.append((nx,ny,sum+1))
        else:
            queue.appendleft((nx,ny,sum))
    