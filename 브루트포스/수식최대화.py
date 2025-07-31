from itertools import permutations
def calculate(N1, N2, op):
    if op=='+': return N1+N2
    elif op=='-': return N1-N2
    elif op=='*': return N1*N2

def solution(expression):
    answer = 0
    # 완전 탐색
    ops = [char for char in expression if char in '+-*' ]

    for op in "-*+":
        expression = expression.replace(op, " ")
    num = expression.split()
    num = list(map(int, num))

    for priority in permutations(set(ops), len(set(ops))):
        num_tmp = num[:]
        ops_tmp = ops[:]
        for op in priority:
            while op in ops_tmp:
                idx = ops_tmp.index(op)
                N1, N2 = num_tmp[idx], num_tmp[idx+1]
                num_tmp[idx] = calculate(N1, N2, op)
                num_tmp.pop(idx+1)
                ops_tmp.pop(idx)
        answer = max(abs(answer),abs(num_tmp[0]))
    return answer

print(solution("100-200*300-500+20"))