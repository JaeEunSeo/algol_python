# 구명보트

def solution(people, limit):
    answer = 0
    people = sorted(people)
    start, end = 0, len(people)-1

    while start <= end:
        if people[start] + people[end]<=limit:
            start += 1
        end -= 1
        answer += 1    
        
    return answer

print(solution([100,100,50,40],140))