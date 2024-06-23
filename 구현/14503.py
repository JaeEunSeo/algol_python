# 로봇 청소기
# 바라보는 방향 구현 : target 좌표 지정

flag = True
N, M = map(int, input().split())
c,r,d = map(int, input().split())

dy = [-1,0,1,0]
dx = [0,1,0,-1]
cnt = 0
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

while True:
    flag = False
    # c: y축(0), r: x축(1)
    if graph[c][r]==0:
        cnt += 1
        # 청소
        graph[c][r] = 2
    # 주변 4칸 중 청소된 빈 칸 있는지 확인
    for i in range(4):
        ny = c + dy[i]; nx = r + dx[i]
        if graph[ny][nx] == 0:
            flag = True
    # 청소할 빈칸이 없으면 후진한다.
    if not flag:
        c -= dy[d]; r -= dx[d]
        if graph[c][r] == 1:
            break
        continue
    elif flag:
        d = (d+4)%4-1
        if graph[c+dy[d]][r+dx[d]]==0:
            c += dy[d]; r += dx[d]
print(cnt)