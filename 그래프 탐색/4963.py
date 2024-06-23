# 섬의 개수
# bfs로 Land인 곳까지 전부 찾고, 주위에 Sea밖에 없으면 break
# queue에 넣는 기준 - 정사각형이 1이면 넣는다

from collections import deque

queue = deque()
# 행 접근 => H, 열 접근 => W graph[H][W]

def bfs(x,y):
    global cnt
    dx = [-1,1,-1,1,0,0,-1,1]
    dy = [0,0,1,1,-1,1,-1,-1]
    while queue:
        x, y = queue.popleft()
        for _ in range(8):
            # x: 행, y : 열
            nx = dx[_]+x
            ny = dy[_]+y
            if (nx>=0) and (nx<H) and (ny>=0) and (ny<W):
                if graph[nx][ny] == 1:
                    queue.append([nx,ny])
                    graph[nx][ny] = -1
                elif graph[nx][ny] == 0:
                    continue
    cnt += 1

cnt_list = []
while True:
    cnt = 0
    W, H = map(int, input().split())
    if W==0 and H==0:
        break
    graph = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                queue.append([i,j])
                bfs(i,j)
    cnt_list.append(cnt)

for _ in cnt_list:
    print(_)


