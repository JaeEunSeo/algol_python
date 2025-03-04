# 키로거
# 커서 문제 -> 스택으로 접근할 것
N = int(input())
for _ in range(N):
    keys = input()
    cursor = 0
    left = []
    right = []

    for key in keys:
        if key == '<' and len(left)>0:
            cur = left.pop()
            right.append(cur)
        elif key == '>' and len(right)>0:
            cur = right.pop()
            left.append(cur)
        elif key == '-' and len(left)>0:
            left.pop()
        elif key not in ['<', '>', '-']:
            left.append(key)
    answer = ''.join(left)+''.join(right[::-1])
    print(answer)
    