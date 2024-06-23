import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
for i in range(N):
    heapq.heappush(q, int(input()))

result = 0
while True:
    if len(q) == 1:
        break
    A = heapq.heappop(q)
    B = heapq.heappop(q)
    heapq.heappush(q, A + B)
    result += (A + B)

print(result)