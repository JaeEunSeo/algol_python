from itertools import combinations
N, M = map(int, input().split())
graph = []
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

chickens = []
c_cnt = 0

#치킨집의 인덱스를 모아둔다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            c_cnt += 1
            chickens.append([i,j])

result_lst = []
def dist(map, chickens):
    result = 0
    if len(chickens)==0:
        return
    for i in range(N):
        for j in range(N):
            if map[i][j]==1:
                dist = []
                for c in chickens:
                    #print(c)
                    a, b = c[0], c[1]
                    dist.append((abs(i-a)+abs(j-b)))
                result += min(dist)
    result_lst.append(result)
    return


for k in combinations(chickens,c_cnt-M):
    tmp_map = graph
    tmp_chickens = chickens.copy()
    # 새로운 map 생성
    for j in k:
        a, b = map(int, j)
        #치킨집 폐업시킴.
        tmp_map[a][b] = 0
        tmp_chickens.remove(j)
        # 각 집마다 거리 계산
    dist(tmp_map, tmp_chickens)
    

print(min(result_lst))