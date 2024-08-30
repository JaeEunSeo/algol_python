import sys

N = int(sys.stdin.readline())

towers = list(map(int,input().split()))
# queues = deque()

# for i in range(len(towers)):
#     cnt = 0
#     for j in range(i, -1, -1):
#         if towers[j] > towers[i]:
#            cnt = j+1
#            break
#     queues.append(cnt) 

# print(*queues)

stack = []
answers = []
for i in range(N):
    answer = 0
    while stack:
        if stack[-1][1] > towers[i]:
            answer = stack[-1][0] + 1
            break
        else:
            stack.pop()
    answers.append(answer)
    stack.append([i, towers[i]])

print(*answers)