import sys
from collections import defaultdict

input = sys.stdin.readline

M, N = map(int, input().split())
counter = defaultdict(int)

for _ in range(M):
    universe = list(map(int, input().split()))
    sorted_uni = sorted(universe)
    rank_map = {}
    for i, num in enumerate(sorted_uni):
        if num not in rank_map:
            rank_map[num] = i
    print(rank_map)
    rank_seq = tuple(rank_map[num] for num in universe)
    counter[rank_seq] += 1

answer = sum(cnt * (cnt - 1) // 2 for cnt in counter.values())
print(answer)