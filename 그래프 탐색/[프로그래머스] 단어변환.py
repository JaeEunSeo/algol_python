from collections import deque
# 두 문자열의 차이가 1인 경우 True 반환 - 그래프 추가 가능
def count(A, B):
    cnt = 0
    for i in range(len(A)):
        if A[i]!=B[i]:
            cnt += 1
    #print(A, B, cnt)
    return True if cnt == 1 else False

def search(begin, words):
    next_nodes = []
    for w in words:
        if count(begin, w):
            next_nodes.append(w)
            words.remove(w)
    return next_nodes, words

def solution(begin, target, words):
    answer = 0; flag = False
    # graph : node와 한 문자만 중복되는 node들이 연결되어있음 - 방향성 X
        # example - "hit" - "hot" - "dot", "lot" ... "dog", "log" - "cog"
    # 비교 방법 : 문자열을 파싱해서 count -> 1개인 경우 추가한다.
    queue = deque([[begin]])
    if begin in words: 
        words.remove(begin)
    visited = {w:False for w in words}
    if target not in words:
        flag = True
    while not flag:
        root = queue.popleft()
        tmp = []
        for r in root:
            if r==target:
                
                flag = True
            next_nodes, words = search(r, words)
            tmp.extend(next_nodes)
        queue.append(tmp)
        if not flag:
            answer += 1
    
    return answer