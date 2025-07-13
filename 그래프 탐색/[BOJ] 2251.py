# 8 9 10
###########
# 8 2 0
# 0 2 8
# 0 8 2
# 0 9 1

# 가능한 경우의 수가 한정적이다. 0 2 8 / 0 1 9 / 0 0 10
# 용량을 확인해야됨. 0 8 2 / 0 9 1
from collections import deque
A,B,C = map(int, input().split())
size = [A,B,C]
# queue에 넣는다. pop해서 나온 걸 토대로, 가능한 애들을 queue에 넣는다. 그 와중에 A=0인 애들은 answer에도 넣는다.
# visited도 만든다.
queue = deque([[0,0,C]])
answer = []
visited = [[0,0,C]]
move = [[0,2],[0,1],[2,1],[2,0],[1,2],[1,0]]

answer.append(C)
while queue:
    cur = queue.popleft()
    for s, e in move:
        next = cur.copy()
        if next[s]>0:
            next[e] += next[s]
            next[s] = 0
            if next[e] > size[e]:
                next[s] += (next[e] - size[e])
                next[e] = size[e]
        if (next not in visited):
            visited.append(next)
            queue.append(next)
            if (next[0] == 0) and (next[2] not in answer):
                answer.append(next[2])
answer.sort()
for i in answer:
    print(i, end=' ')