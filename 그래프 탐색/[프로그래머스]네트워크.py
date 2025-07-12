def solution(n, computers):
    answer = 0
    # 덩어리 여러 개 찾기
    # stack에 연결된 j 추가
    # 전역 visited 필요
    visited = [False] * n
    
    def dfs(stack):
        nonlocal visited
        while stack:
            i = stack.pop()
            for j in range(n):
                if j==i:
                    continue
                if not visited[j] and computers[i][j]:
                    stack.append(ja)
                    visited[j] = True
                    
    for idx in range(n):
        if not visited[idx]:
            stack=[idx]
            dfs(stack)
            answer += 1
                
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))