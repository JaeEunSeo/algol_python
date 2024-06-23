# 그래프 탐색이 중요한 문제

N, k = map(int, input().split())

start = 0
digit = 1
nine = 9

# nine : 9, 90, 900, 9000 ...
# digit : 1, 2, 3, 4 ...
while k>nine*digit:
    k -= (digit * nine)
    start = start + nine
    nine = nine * 10
    digit += 1

# start : 시작하는 자리수 => 이 수에 전진할 만큼 더해준다.
# k : 현재 자리 수에서 전진할 만큼의 수
result = (start+1) + (k-1)//digit

if result>N:
    print(-1)
else: print(str(result)[(k-1)%digit])