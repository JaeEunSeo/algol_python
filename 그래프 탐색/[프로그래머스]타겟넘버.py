# 타겟 넘버 만드는 방법 수 return
# 시작점: 두 개

def solution(numbers, target):
    answer = 0
    d_sign = [-1,1]
    n_sum = 0
    stack = []

    def dfs(i):
        nonlocal n_sum, answer
        if i == len(numbers):
            if n_sum == target:
                answer += 1
            return
        for sign in d_sign:
            new = sign*numbers[i]
            n_sum += new
            stack.append(new)
            dfs(i+1)
            stack.pop()
            n_sum -= new
    
    dfs(0)
    return answer

print(solution(numbers=[4,1,2,1],target=4))