N, D = map(int, input().split())
shortcuts = []
dist = [_ for _ in range(D+1)]

for _ in range(N):
    shortcut = list(map(int,input().split()))
    if (shortcut[1] <= D) and (shortcut[1]-shortcut[0]>shortcut[2]):
        shortcuts.append(shortcut)

# sort 1: 시작점
shortcuts.sort(key= lambda x:x[0])
shortcuts.sort(key= lambda x:x[1])
# 끝나는 지점을 기준으로 더 가까우면 갱신
for choice in shortcuts:
    s, e, d = choice
    if dist[s]+d < dist[e]:
        reduced = dist[e]-dist[s]-d
        for i in range(e,D+1):
            dist[i] = dist[i]-reduced

print(dist[-1])