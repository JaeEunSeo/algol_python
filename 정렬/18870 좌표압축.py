N = int(input())
lst = list(map(int, input().split()))

tmp = sorted(lst)
map = dict()
i = 0
for value in tmp:
    if value in map:
        continue
    map[value] = i
    i += 1

for k in lst:
    if k in map:
        print(map[k], end=' ')