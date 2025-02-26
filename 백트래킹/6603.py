# 로또

def dfs(arr, s, visited):
    if len(arr) == 6:
        for i in range(6):
            print(arr[i], end=' ')
        print()
        return 
    tmp_visited = visited.copy()
    for i in range(len(tmp_visited)):
        if not tmp_visited[i]:
            tmp_visited[i] = True
            dfs(arr+[s[i]], s, tmp_visited)

while True:
    inputs = list(map(int, input().split()))
    k, s = inputs[0], inputs[1:]
    if k == 0: break

    visited = [False] * len(s)
    dfs([], s, visited)
    print()