from collections import deque

N, K = map(int, input().split())

queue = deque()
queue.append([N,0])
visited = [0] * 100001


while queue:
    X, sec = queue.popleft()
    if X==K:
        print(sec)
        break
    sec += 1
    cur = [X*2, X-1, X+1]
    for i in range(len(cur)):
        X = cur[i]
        if X<0 or X>100000:
            continue
        if visited[X] == 1:
            continue
        if i==0:
            queue.append([X,sec-1])
        else:
            #print(X,sec)
            queue.append([X,sec])
        visited[X] = 1