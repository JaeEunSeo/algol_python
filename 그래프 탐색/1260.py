from collections import deque
N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

visited = [False] * (N+1)
visited2 = visited.copy()

for i in range(1,M+1):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in range(1, N+1):
        if graph[i][start] == 1 and not visited[i]:
            dfs(i)

def bfs(start):
    queue = [start]
    visited2[start] = True
    print()
    while queue:
        start = queue.pop(0)
        print(start, end=' ')
        for i in range(1, N+1):
            if graph[i][start] == 1 and not visited2[i]:
                queue.append(i)
                visited2[i] = True
                

dfs(V)
bfs(V)