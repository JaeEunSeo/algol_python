# 회의실 배정
N = int(input())
meetings = []

for i in range(N):
    s, e = map(int, input().split())
    meetings.append([s,e])

meetings.sort(key = lambda x:(x[1], x[0]))
prev_end = 0

result = 0
for s, e in meetings:
    if prev_end <= s:
        result += 1
        prev_end = e


print(result)