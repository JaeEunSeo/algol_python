# 완전 이진 트리
K = int(input())
tree = list(map(int, input().split()))

level = 0
result = []
# 인덱스로 접근할 때 pop되면 안되므로 copy된 tree 생성 => 해당 tree는 레벨 올라갈 때마다 새로 copy
while level < K:
    tree_copy = tree.copy()
    mini_result = []
    i = 0
    #print(tree_copy)
    while i<len(tree_copy):
        mini_result.append(tree_copy[i])
        tree.remove(tree_copy[i])
        i += 2
    result.append(mini_result)
    level += 1

for r in reversed(result):
    print(*r)