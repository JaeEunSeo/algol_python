# 인접 리스트로 연결연결 확인확인
# DFS
N = int(input())
M = int(input())

maps = [[0]*N for _ in range(N)]
flag = 0

for i in range(N):
   # i : 도시
   # j : 연결된 도시들
    lst = list(map(int, input().split()))
    tmp = []
    for j in range(len(lst)):
        if lst[j]==1:
            maps[i][j] = maps[j][i] = 1


# 방문 순서가 연속인 두 도시를 입력받는다.
# 사이클 처리
def dfs(start, end, visited):
    global flag
    visited[start] = 1
    # 재귀로 maps에 저장된 해당 리스트 호출
    # end 인자에는 매번 같은 값이 들어감 => 해당 호출에서 가능한지 확인해야 함
    for i in range(N):
        if maps[start][end] == 1:
            flag = 1
            return
        if maps[start][i] == 0:
            continue
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, end, visited)
    return

results = []
plan = list(map(int, input().split()))

for i in range(len(plan)-1):
    flag = 0
    visited = [0] * N
    dfs(plan[i]-1, plan[i+1]-1, visited)
    results.append(flag)

if 0 not in results or len(set(plan))==1:
    print('YES')
else:
    print('NO')