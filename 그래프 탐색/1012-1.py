from collections import deque
import sys
# 배추의 위치 저장 => graph에 1로 저장
# 시작점 지정
    # cabbage[0]으로 지정
# dx, dy로 queue에 저장하며 순회하며 visited = True로 설정
    # cabbage에서 x, y 값 remove
# 더 이상 접근 가능한 배추 없는 경우 cnt += 1

T = int(input())

def start():
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0
    for _ in range(K):
        a,b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue = deque([(i,j)])
                graph[i][j] = 0
                while queue:
                    x,y = queue.popleft()
                    for a in range(4):
                        nx = x + dx[a];ny = y + dy[a]
                        if not (0 <= nx < N) or not (0 <= ny < M):
                            continue
                        if graph[nx][ny] == 1:
                            queue.append((nx,ny))
                            graph[nx][ny] = 0
                    
                cnt += 1           
    return cnt

for i in range(T):
    print(start())