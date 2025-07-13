from collections import deque

def solution(N, K):
    queue = deque([[N, 0]])
    visited = [False]*1000001
    while queue:
        X, sec = queue.popleft()
        visited[X] = True
        if X == K:
            break
        cands = [[X*2,sec], [X-1, sec+1], [X+1, sec+1]]
        for c in cands:
            if 0<=c[0]<=100000 and not visited[c[0]]:
                queue.append(c)
    return sec

N, K = map(int, input().split())
print(solution(N,K))