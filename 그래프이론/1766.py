# 문제집
# queue, parent list
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    graph[A].append(B)

result = []

def topology_sort():
    queue = deque()
    queue = []
    for i in range(1, N+1):
        if indegree[i]==0:
            queue.append(i)
            #visited[i] = 1
    #print(queue)

# queue에 진입차수가 0인 노드들이 들어간 상태
    while queue:
        #queue = deque(set(queue))
        queue.sort()
        cur = queue.pop(0)
        result.append(cur)

        for node in graph[cur]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)

        graph[cur] = []

topology_sort()
print(*result)
                