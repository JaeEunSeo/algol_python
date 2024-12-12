# 드래곤 커브

N = int(input())

'''
90도 회전 함수
-------------
parameters:
direction - 시작점부터 끝점까지 차례대로 입력되어 있는 edge list
return: 회전한 후의 인접 리스트
'''
def rotate_direction(direction:list) -> list:
    for i in range(len(direction)-1,-1,-1):
        direction.append((direction[i]+1)%4)
    return direction

def move_forward(x,y,d):
    if d == 0:
        nx, ny = x+1, y
    if d == 1:
        nx, ny = x, y-1
    if d == 2:
        nx, ny = x-1, y
    if d == 3:
        nx, ny = x, y+1
    return (nx,ny)

def find_square(nodes:list)-> int:
    count = 0
    for x, y in nodes:
        if (x+1, y) in nodes and (x, y+1) in nodes and (x+1, y+1) in nodes:
            count += 1
    return count


nodes = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    directions = [d]
    for r in range(g):
        directions = rotate_direction(directions)
    route = [(x,y)]
    for d in directions:
        x, y = move_forward(x,y,d)
        route.append((x,y))
    nodes = list(set(nodes+route))

print(find_square(nodes))