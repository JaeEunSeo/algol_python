# 큰수만들기

def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    answer = num[:len(number)-k]
    return answer