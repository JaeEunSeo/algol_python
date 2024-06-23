#15649

N, M = map(int, input().split())
graph = [(_+1) for _ in range(N)]
visited = [False] * (N+1)
out = []

def dfs():
    if len(out)==M:
        print(' '.join(map(str, out)))
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            out.append(i)
            #print(len(out))
            dfs()
            visited[i] = False
            out.pop()

dfs()