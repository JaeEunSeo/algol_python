from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            cx, cy = i, j

class shark:
    def __init__(self):
        self.size = 2
        # acc : 지금까지 먹은 물고기 수 
        self.acc = 0

baby = shark()
dy = [-1,0,1,0]
dx = [0,-1,0,1]

def bfs(a,b):
    visited = [[0] * N for _ in range(N)]
    cand = []
    queue = deque([[a,b]])
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if (nx<0 or ny<0 or nx>=N or ny>=N) or visited[nx][ny]!=0:
                continue

            '''
            cand 후보군에 들어갈 수 있는 경우는 물고기가 본인보다 크기가 작을 경우만 존재한다.
            지나갈 수 있는 길인 경우 queue에 nx,ny를 append만 한다.
            지나갈 수 없는 경우 다음 nx,ny를 조회한다.
            '''

            if 0<graph[nx][ny]<baby.size:
                # 지나갈 수 있는 칸일 경우
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
                # 후보군의 첫번째 원소 : 도달시간, 
                cand.append([visited[x][y],nx,ny])
            elif baby.size < graph[nx][ny]:
                # 지나갈 수 없는 칸인 경우
                continue
            else:
                # 지나갈 수는 있지만 후보군이 아닌 경우
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

    return sorted(cand, key=lambda x:(x[0],x[1],x[2]))

cnt = 0
# 잡아먹을 수 있는 물고기가 없을 때까지
while True:
    cand = deque(bfs(cx,cy))
    if not cand:
        break

    cost, x, y = cand.popleft()
    cnt += cost
    baby.acc += 1

    if baby.size == baby.acc :
        baby.size += 1
        baby.acc = 0

    graph[cx][cy] = 0
    cx,cy = x,y

print(cnt)