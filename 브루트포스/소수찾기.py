from itertools import permutations

def is_prime(k):
    for i in range(2, int(k**0.5+1)):
        if k%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    visited = []
    for n in range(1,len(numbers)+1):
        perms = set(permutations(numbers, n))
        for p in perms:
            k = int(''.join(p))
            if k in [0,1] or k in visited:
                continue
            if is_prime(k):
                answer += 1
            visited.append(k)
    return answer

print(solution("17"))