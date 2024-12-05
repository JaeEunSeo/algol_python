# 백준 골드3 최소비용 구하기2

import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = n * 100000+1

graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
route = [[] for _ in range(n+1)]

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0
    while queue:
        d, now = heapq.heappop(queue)
        if d > dist[now]:
            continue
        # 인접 도시 업데이트
        for cur in graph[now]:
            cost = d + cur[1]

            if dist[cur[0]] > cost:
                route[cur[0]] = now  # 직전 도시를 저장한다.
                dist[cur[0]] = cost
                heapq.heappush(queue, (cost, cur[0]))

    tmp = end
    path = [end]

    while tmp!=start:
        tmp = route[tmp]
        path.append(tmp)
    path.reverse()
    
    return dist, path
            

for i in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))

start, end = map(int, input().split())

dist, path = dijkstra(start, end)
print(dist[end])
print(len(path))
print(*path)