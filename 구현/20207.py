# 백준 달력

N = int(input())
schedule = []
calendar = [[False] * (N) for _ in range(366)]

def get_max_seq(day, calendar):
    max_seq = 0
    while True in calendar[day]:
        tmp = [sc for sc in calendar[day] if sc]
        max_seq = max(max_seq,len(tmp))
        day +=1
        if day >= 366:
            return day, max_seq
    # 끝나는 날짜와 Max_seq 반환
    return day, max_seq


for _ in range(N):
    S, E = map(int, input().split())
    schedule.append((S,E))

schedule.sort(key=lambda x:(x[0], -x[1]))

for s in schedule:
    S, E = s
    idx = next((j for j in range(N) if not calendar[S][j]))
    for i in range(S,E+1):
        calendar[i][idx] = True

answer = 0
day = 1
while day < 366:
    if calendar[day][0]:
        end_day, max_seq = get_max_seq(day, calendar)
        answer += (end_day-day) * max_seq
        day = end_day
    else: day += 1

print(answer)