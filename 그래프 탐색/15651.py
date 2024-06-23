#15651

N, M = map(int, input().split())

graph = [(_+1) for _ in range(N)]
visited = [False] * (N+1)
out = []

def dfs(n):
    if (n>M):
        print(' '.join(map(str, out)))
        return
    for i in range(1,N+1):
        out.append(i)
        dfs(n+1)
        out.pop()

dfs(1)