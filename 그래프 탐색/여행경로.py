from collections import deque
def solution(tickets):
    answer = []
    # 항공권 사용 여부
    visited = [False] * len(tickets)

    def dfs(start, path):
        if len(path) == len(tickets)+1:
            answer.append(path)
            return 
        for idx, ticket in enumerate(tickets):
            if (ticket[0] == start) and (not visited[idx]):
                visited[idx] = True
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])

    answer.sort()
    return answer[0]

print(solution([["ICN", "D"], ["D", "ICN"], ["ICN", "A"]]))