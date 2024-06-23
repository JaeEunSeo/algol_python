# 단지번호붙이기 - BFS

from collections import deque
N = int(input())
graph = []
global cnt

for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    # 값이 2 이상일 경우 : 건너뛰어야됨
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<N) and (0<=ny<N):
                dfs(nx,ny)
        return True
    return False
    
count = 0
num = 0
result = []
for i in range(N):
    for j in range(N):
        if dfs(i,j):
           result.append(count)
           num += 1
           count = 0

result.sort()
print(num)
for i in result:
    print(i)