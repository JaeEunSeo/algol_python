import sys
input = sys.stdin.readline


def find(x, parent):
    # 만일 parent가 자기자신으로 설정된 경우, 그냥 자기 자신 값 return
    if parent[x]!=x:
        # 아닐 경우, 부모노드 탐색 후 return
        return find(parent[x], parent)
    return x

# 자식 수가 더 많은 쪽으로 union

def union(a, b, parent):
   #a, b = 각각 a와 b의 부모 노드
   a = find(a, parent)
   b = find(b, parent)
   if a != b: 
        if a < b :
           parent[b] = a
        else:
           parent[a] = b

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
child = [1 for i in range(V+1)]
visited = [False for i in range(V+1)]
edges = []
result = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

# find 해서 전부 같은 노드를 parent로 둘 때까지 해야됨..

# 간선 작은 순서부터 정렬
edges.sort()

for edge in edges:
    cost, A, B = edge
    if find(A, parent)!=find(B, parent):
        visited[A] = True
        visited[B] = True
        union(A, B, parent)
        result += cost



print(result)