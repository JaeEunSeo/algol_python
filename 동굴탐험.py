from collections import deque


def solution(n, path, order):
    answer = True
    graph = [[] for _ in range(n)]
    before, after = {}, {}
    visited = [False] * n

    for p in path:
        a, b = p
        graph[a].append(b)
        graph[b].append(a)
    for ord in order:
        if ord[1] == 0:
            return False
        before[ord[1]] = ord[0]
        
    stack = [0]
    while stack:
        node = stack.pop()
        if node in before and not visited[before[node]]:
            after[before[node]] = node
            continue
        
        visited[node] = True
        for next in graph[node]:
            if not visited[next]:
                stack.append(next)

        if node in after:
            stack.append(after[node])

    if False in visited:
        answer = False

    return answer

print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[8,5],[6,7],[4,1]]))