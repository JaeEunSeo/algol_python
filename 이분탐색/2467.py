# 용액
N = int(input())
solutions = list(map(int, input().split()))

left, right = 0, N-1
answer = float('inf')
while left < right:
    mid = (left+right)//2
    sum = solutions[left]+solutions[right]
    if abs(sum) < abs(answer):
        answer = sum
        cur = [solutions[left], solutions[right]]
    if sum > 0:
        right -= 1
    elif sum < 0:
        left += 1
    else:
        break

print(*cur)