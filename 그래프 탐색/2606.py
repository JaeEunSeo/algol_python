N = int(input())
k = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]
virus = [0] * (N+1)

for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(V):
    for i in range(1, len(graph[V])):
        linked = graph[V][i]
        # 감염 안됐는데 연결되어있는 경우
        if (virus[i] == 0 and linked == 1):
            virus[i] = 1
            dfs(i)

dfs(1)
result = 0
for i in range(2,N+1):
     if virus[i] == 1 :
         result += 1

print(result)