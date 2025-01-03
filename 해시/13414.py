# 수강신청
import sys
K, L = map(int, input().split())
queue = dict()

for _ in range(L):
    student_num = sys.stdin.readline().rstrip()
    if student_num in queue:
        queue.pop(student_num)
    queue[student_num] = True

for student in list(queue.keys())[:K]:
    print(student)