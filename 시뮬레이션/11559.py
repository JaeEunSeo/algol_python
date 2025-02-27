# 뿌요뿌요

field = []
for _ in range(12):
    line = list(_ for _ in input())
    field.append(line)
N = len(field)
cnt = 0
dx, dy = [-1,1,0,0], [0,0,-1,1]

def find_puyo(x,y,stack,visited) -> list:
    visited[x][y] = 1
    stack.append((x,y))
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0<= ax < N and 0<= ay < 6:
            if visited[ax][ay] == 1:
                continue
            elif visited[ax][ay]==0:
                visited[ax][ay] = 1
                if field[ax][ay] == field[x][y]:
                    stack = find_puyo(ax,ay,stack,visited)
    return stack

def fall():
    for y in range(6):
        for x in range(N-2, -1, -1):
            ax = x
            if field[x][y] == '.': continue
            while ax < N-1:
                if field[ax+1][y]=='.':
                    field[ax+1][y] = field[ax][y]
                    field[ax][y] = '.'
                ax += 1

        if field[N-1][y]=='.':
            for x in range(N-1, 0, -1):
                field[x][y] = field[x-1][y]

def pop_field(pop_stack):
    for xy in pop_stack:
        x, y = xy[0], xy[1]
        field[x][y] = '.' # 저장 좌표 pop
    fall()

while True:
    stack = []
    for i in range(N):
        for j in range(6):
            visited = [[0] * 6 for _ in range(N)]
            if field[i][j]=='.': continue
            pop_stack = find_puyo(i,j,[],visited)
            if len(pop_stack)>=4:
                stack.extend(pop_stack)

    if len(stack)==0:
        break
    pop_field(stack)
    cnt += 1

print(cnt)