H, W = map(int, input().split())
blocks = list(map(int, input().split()))

world = [[0] * W for _ in range(H)]
floor = []

for i in range(W):
    for j in range(blocks[i]):
        world[j][i] = 1

floors = []
start, end = 0, W-1

for i in range(H):
    for j in range(start,end+1):
        if world[i][j]==1:
            floor.append(j)
    if len(floor) <= 1:
        break
    floors.append(floor)
    start, end = floor[0], floor[-1]
    floor = []

cnt = 0

for floor in floors:
    for i in range(len(floor)-1):
        cnt += floor[i+1]-floor[i]-1

print(cnt)
