from collections import deque
N = int(input())

tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
parents = []
for _ in range(N-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)

# 1번부터 bfs 시작
queue = deque([1])
while queue:
    cur = queue.popleft()
    visited[cur] = True
    for node in tree[cur]:
        if not visited[node]:
            parents.append((node, cur))
            queue.append(node)

parents.sort(key=lambda x:x[0])
for i in range(len(parents)):
    print(parents[i][1])