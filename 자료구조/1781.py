import sys
import heapq

input = sys.stdin.readline
N = int(input())
q = []
table = []

for i in range(N):
    t, cost = map(int, input().split())
    # 컵라면의 수를 기준으로 우선순위 정렬
    table.append((t, cost))
table.sort() # 시간 순으로 정렬한다.

for i in table:
    heapq.heappush(q, i[1])
    # 시간을 넘긴 경우 pop.
    if i[0] < len(q):
        a = heapq.heappop(q)
        
print(sum(q))