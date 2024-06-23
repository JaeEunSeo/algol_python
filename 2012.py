import sys
N = int(sys.stdin.readline())
rank = []
for _ in range(N):
    rank.append(int(sys.stdin.readline()))

rank.sort()
cnt = 0
for i in range(N):
    if rank[i]!=i+1:
        cnt += abs(rank[i]-(i+1))

print(cnt)