#bfs에서 최대 기간을 구하는 문제는 시작점 (1)을 전부 queue에 넣어두어야 한다.
import copy
from collections import deque
M, N = map(int, input().split())
graph = []

for _ in range(N):
    tomatos = list(map(int,input().split()))
    graph.append(tomatos)

day = copy.deepcopy(graph)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

zero_flag = True #익지 않은 토마토가 있을 경우 true
queue_flag = False

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue_flag = True
            queue.append([i,j])

while queue:
    x,y = queue.popleft()
    for _ in range(4):
        nx = x+dx[_]
        ny = y+dy[_]
        if (nx>=0 and nx<N and ny>=0 and ny<M):
            if graph[nx][ny]==0:
                zero_flag = False
                graph[nx][ny] = 1
                day[nx][ny] = day[x][y] + 1
                #print(nx,ny)
                queue.append([nx,ny])

#print(day)

result = 0
impossible = False

for i in range(N):
    for j in range(M):
        if day[i][j] == 0:
            impossible = True
            break
        result = max(result, day[i][j]-1)

if zero_flag and queue_flag:
    print(0)
elif not impossible:
    print(result)
else:
    print(-1)
