
def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x:x[2])
    parent = [0] * (n+1)
    for _ in range(1,n+1):
        parent[_] = _

    def union(a, b):
        a = find_parent(a, parent)
        b = find_parent(b, parent)
        if a > b:
            parent[a] = b
        if a < b:
            parent[b] = a

    def find_parent(x, parent):
        if parent[x]!=x:
            parent[x] = find_parent(parent[x], parent)
        return parent[x]
    
    
    for c in costs:
        a, b, cost = c
        if find_parent(a, parent)!=find_parent(b, parent):
            union(a,b)
            answer += cost
        
    return answer