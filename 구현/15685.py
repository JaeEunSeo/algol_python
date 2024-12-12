# 드래곤 커브

N = int(input())
dx = [1,0,-1,0]
dy = [0,-1,0,1]

'''
90도 회전 함수
-------------
parameters:
direction - direction list
return: 회전한 이후의 direction list
'''
def rotate_direction(direction:list) -> list:
    for i in range(len(direction)-1,-1,-1):
        direction.append((direction[i]+1)%4)
    return direction

def find_square(nodes:list) -> int:
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
        x, y = x + dx[d], y + dy[d]
        route.append((x,y))
    nodes = list(set(nodes+route))

print(find_square(nodes))