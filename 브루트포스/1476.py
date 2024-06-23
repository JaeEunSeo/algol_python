E, S, M = map(int, input().split())

year = 1
while True:
    if (year-E)%15==0 and (year-S)%28==0 and (year-M)%19==0:
        print(year)
        break
    year += 1

# S의 단위가 가장 크므로, S를 기준으로 순회한다.
    