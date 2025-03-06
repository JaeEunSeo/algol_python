M, N = map(int, input().split())
from itertools import combinations
unis = []

for _ in range(M):
    uni = list(map(int, input().split()))
    tmp = sorted(uni)
    sizes = dict.fromkeys(uni, 0)
    #print(sizes)

    for i in range(N):
        sizes[tmp[i]] = i
    unis.append(list(sizes.values()))

result = 0
combs = combinations(unis,2)
for c in list(combs):
    if c[0] == c[1]:
        result += 1
print(result)