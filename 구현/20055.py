# 컨베이어 벨트 위의 로봇
from collections import Counter, deque

# Trial 3
# => deque rotate
N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([False] * N)
result = 0

# 벨트 회전
while True:
    belt.rotate(1)
    robots.rotate(1)
    # 로봇의 이동 -> 마지막 칸 로봇 하차
    robots[-1] = False
    if True in robots:
        # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동.
        # 로봇이 이동하기 위해서는 그 칸에 로봇이 없고, 내구도가 1 이상 남아 있어야 함
        for i in range(N-2, -1, -1):
            if robots[i] and not robots[i+1] and belt[i+1]>=1:
                robots[i+1] = True
                robots[i] = False
                belt[i+1] -= 1
    # 로봇의 이동 -> 마지막 칸 로봇 하차
    robots[-1] = False
    if not robots[0] and belt[0] >= 1:
        robots[0] = True
        belt[0] -= 1
    result += 1

    if belt.count(0) >= K:
        break

print(result)


# Trial 2

# robots, squares = [False for i in range(N)], []
# class Square:
#     def __init__(self, ability, loc):
#         self.ability = ability
#         self.loc = loc
#         self.robot = False

# for i in range(2*N):
#     squares.append(Square(ability=tmp[i], loc=i))

# robots[0] = True
# squares[0].ability -= 1
# result = 0
# while Counter([square.ability for square in squares if square.ability <= 0]):
#     # 칸 회전
#     for i in range(2*N-1):
#         squares.loc += 1
#         if squares.loc == 2 * N: squares.loc = 0

#     # 로봇 이동
#     for i in range(N-1):
        

# print(result)



# Trial 1
# def count_zero(belt):
#     cnt = 0
#     for b in belt:
#         if b == 0: cnt += 1
#     return cnt

# cur = 0
# result = 0
# while belt[cur] > 0:
#     belt[cur] -= 1

#     if count_zero(belt) >= K:
#         break
#     print(cur, belt[cur])
#     result += 1
    
#     if cur == N-1: next = 0
#     else: next = cur+1

#     if belt[next] == 0:
#         next = cur

#     cur = next

# print(result)
