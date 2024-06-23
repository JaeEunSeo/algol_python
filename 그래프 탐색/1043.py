# 거짓말

N, M = map(int,input().split())

# 0 ~ N까지 저장
roots = [i for i in range(N+1)]

for i in list(map(int, input().split()))[1:]:
    # 진실을 아는 사람의 부모 - 0으로 설정
    roots[i] = 0

def union(x, y):
    x = find(x); y = find(y)
    if x < y :
        roots[y] = x
    else:
        roots[x] = y

# 재귀함수로 구현
def find(x):
    if roots[x]!=x:
        return find(roots[x])
    return x

parties = []
for i in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party)
    if len(party)>1:
    # 동일 파티에 속한 사람들은 union
        for j in range(1, len(party)):
            # 루트 값 변경
            union(party[j-1], party[j])

cnt = 0
for party in parties:
    for p in party:
        if find(roots[p])!=0:
            # 거짓말이 가능한 파티이다.
            cnt += 1
            break
    
print(cnt)