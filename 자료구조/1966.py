# 프린터 큐
# 큐 : 튜플들을 저장한다
from collections import deque

tc = int(input())

def printer(N, target):
    queue = deque()
    status = list(map(int,input().split()))
    if N==1:
        return 1
    for i in range(len(status)):
        # 각 문서의 번호와 중요도를 큐에 저장한다.
        queue.append((i, status[i]))
    cnt = 0
    max_importance = max(status)
    while queue:
        cur = queue.popleft()
        # 중요도가 작은 경우
        if cur[1] < max_importance:
            queue.append(cur)
            continue
        else:
            # 가장 중요도가 높은 문서를 출력했다.
            cnt += 1
            if queue:
                max_importance = max(item[1] for item in queue)
            if cur[0] == target:
                return cnt
            

for _ in range(tc):
    N, M = map(int, input().split())
    print(printer(N, M))