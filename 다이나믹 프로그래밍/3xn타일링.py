def solution(n):
    if n == 4:
        return 11
    elif n == 2:
        return 3
    answer = 0
    n = n/2 - 2
    cur = (3,11)
    while n>0:
        cur = (cur[1],cur[1]*4-cur[0])
        n-=1
    return cur[1]%1000000007

print(solution(6))