# N-Queen
# 좌우 상하 대각선에 위치 X

# 1. 일단 놓는다 (1)
# 2. 검증한다 (상하좌우대각선 확인 - 함수로) 총 8개 가능
# 3. 가능하면 1, 불가능하면 -1 처리한다.

N = int(input())

col = [0] * (N+1)
cnt = 0

def n_queens(i, col):
    global cnt
    n = len(col) -1
    if (promising(i, col)):
        if (i == n):
            cnt += 1      
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

def promising (i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag


n_queens(0,col)
print(cnt)