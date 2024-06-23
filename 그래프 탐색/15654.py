#15654
N, M = map(int, input().split())
graph = sorted(map(int,input().split()))
#print(graph)
check = [False] * N
out = []

def track():
    if len(out) == M:
        print(' '.join(map(str,out)))
        return
    for i in range(N):
        if check[i]:
            continue
        out.append(graph[i])
        check[i] = True
        track()
        check[i] = False
        out.pop()
track()