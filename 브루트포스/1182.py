# 부분수열의 합

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0

#cur : index, total: 합
def backtracking(cur, total):
    global cnt
    if (total==S) and cur!=0:
        cnt += 1
        
    for i in range(cur,N):
        total += numbers[i]
        backtracking(i+1, total)
        total -= numbers[i]
    


backtracking(0,0)
print(cnt)