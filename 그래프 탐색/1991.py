# 트리 순회

# 딕셔너리 선언
tree = {}

N = int(input())

for i in range(N):
    nodes = list(map(str, input().split()))
    tree[nodes[0]] = [nodes[1],nodes[2]]

def preorder(root):
    if root=='.':
        return
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])
    return

def inorder(root):
    if root=='.':
        return
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])
    return

def postorder(root):
    if root=='.':
        return
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')
    return

preorder('A')
print()
inorder('A')
print()
postorder('A')