import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
costs = [1e9 for _ in range(N+1)]

def dijkstra(start, B):
    global costs
    q = []
    heapq.heappush(q, (0, start))
    while q:
        # val이 낮은, 즉 비용이 적은 node부터 확인
        val, node = heapq.heappop(q)
        if costs[node] < val:
            continue
        for node, cost in graph[node]:
            # 인접노드까지 가는 데에 걸리는 비용
            new_cost = val + cost
            if new_cost >= costs[node]: continue
            if new_cost < costs[node]:
                costs[node] = new_cost
                heapq.heappush(q, (new_cost, node))
    return costs[B]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append([b,t])
    
A, B = map(int, input().split())
costs[A] = 0
print(dijkstra(A, B))    