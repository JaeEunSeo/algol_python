# 큐 2
import sys
N = int(input())

from collections import deque
queue = deque()

def remote(string):
    command = string.split(' ')
    if len(command)==2:
        number = command[1]
        command = command[0]
    else:
        command = command[0]

    if command=='push':
        queue.append(number)
    elif command=='pop':
        if not queue:
            print(-1)
        else:
            a = queue.popleft()
            print(a)
    elif command=='size':
        print(len(queue))
    elif command=='empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command=='front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command=='back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
        
for i in range(N):
    command = sys.stdin.readline().strip()
    remote(command)