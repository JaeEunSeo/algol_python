#익어있는 토마토(1) 위치 전부 저장, stack에 넣고 시작
#방향 : [-1,-1,1,1,0,0]
import sys
sys.setrecursionlimit(10**6)

dx, dy, dz = [-1,1,0,0,0,0], [0, 0, 0, 0, -1,1], [0,0,-1,1,0,0]
M, N, H = map(int, input().split())
boxes = []
stack = []
tmp_stack = []
for h in range(H):
    box = []
    for n in range(N):
        floor = list(map(int,input().split()))
        for m in range(M):
            if floor[m] == 1:
                tmp_stack.append((h,n,m))
        box.append(floor)
    boxes.append(box)
stack.append(tmp_stack)

def dfs(cnt):
    new = []
    cur = stack.pop(-1)
    for h, n, m in cur:
        for i in range(6):
            nh = h + dz[i]
            nn = n + dy[i]
            nm = m + dx[i]
            if 0<=nh<H and 0<=nn<N and 0<=nm<M:
                if boxes[nh][nn][nm] == 0 :
                    boxes[nh][nn][nm] = 1
                    new.append((nh,nn,nm))
    if len(new)==0:
        return cnt
    stack.append(new)
    cnt = dfs(cnt + 1)
    return cnt

answer = dfs(0)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 0:
                answer = -1
                break
print(answer)
        
            
