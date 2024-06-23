from itertools import permutations
N = int(input())
numbers = list(map(int, input().split()))
operation = list(map(int, input().split()))
operations = []
for _ in range(4):
    i = operation[_]
    if _ == 0:
        for j in range(i):
            operations.append('+')
    if _ == 1:
        for j in range(i):
            operations.append('-')
    if _==2:
        for j in range(i):
            operations.append('*')
    if _==3:
        for j in range(i):
            operations.append('%')

ans = []
for k in set(permutations(operations,N-1)):
    result = numbers[0]
    for i in range(N-1):
        if k[i] =='+': # operation 
            result = result + numbers[i+1] #연산하는 숫자
        elif k[i]=='-':
            result = result - numbers[i+1]
        elif k[i]=='*':
            result = result * numbers[i+1]
        elif k[i]=='%':
            if result <0 :
                result = -((-result) // numbers[i+1])
            else:
                result = result // numbers[i+1]

    ans.append(result)

print(max(ans))
print(min(ans))