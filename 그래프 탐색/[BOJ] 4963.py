from collections import deque
import sys
input = sys.stdin.readline

def solution():
    cnt_list = []
    def bfs(x,y):
        queue = deque([[x,y]])
        dx = [-1,0,1,-1,0,1,-1,1]
        dy = [1,1,1,-1,-1,-1,0,0]
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            for _ in range(8):
                nx, ny = x+dx[_], y+dy[_]
                if (0<=nx<h) and (0<=ny<w):
                    if (maps[nx][ny] == 1) and (not visited[nx][ny]):
                        visited[nx][ny] = True
                        queue.append([nx,ny])
        return
    
    while True: 
        cnt = 0
        w, h = map(int, input().split())
        if (w == 0) and (h == 0):
            break
        maps = []
        for _ in range(h):
            m = list(map(int, input().split()))
            maps.append(m)
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        for i in range(h):
            for j in range(w):
                if (maps[i][j] == 1) and (not visited[i][j]):
                    bfs(i,j)
                    cnt += 1
        cnt_list.append(cnt)
    for cnt in cnt_list:
        print(cnt)
    return

solution()