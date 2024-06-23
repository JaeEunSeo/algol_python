# 다익스트라 알고리즘 - 최단경로

import heapq
V, E = map(int, input().split())
start = int(input())
# 연결정보 - 2중 리스트는 느리다.
graph = [[] for _ in range(V+1)]
distance = [int(1e9) for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    cost = []
    heapq.heappush(cost, (0, start))
    while cost:
        dist, cur = heapq.heappop(cost)
        if distance[cur] < dist:
            continue
        for node in graph[cur]:
            # node : 현재 노드와 인접한 노드, 비용
            if dist + node[1] < distance[node[0]]:
                distance[node[0]] = dist+node[1]
                heapq.heappush(cost, (dist+node[1], node[0]))

dijkstra(start)

for i in range(1,V+1):
    if i == start:
        print(0)
        continue
    print(distance[i]) if distance[i]!=int(1e9) else print('INF')