from copy import copy
from collections import deque

N, M, x, y, K = map(int, input().split())

# 바닥면 : 'd' 윗면 : 'b'

dice = {"a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0}

def method_1(dice):
    tmp_dice = dice.copy()
    dice['a'] = tmp_dice['a']
    dice['b'] = tmp_dice['e']
    dice['f'] = tmp_dice['b']
    dice['c'] = tmp_dice['c']
    dice['d'] = tmp_dice['f']
    dice['e'] = tmp_dice['d']
    #print(graph,dice)
    print(dice['b'])
    return dice

def method_2(dice):
    tmp_dice = dice.copy()
    dice['a'] = tmp_dice['a']
    dice['c'] = tmp_dice['c']
    dice['b'] = tmp_dice['f']
    dice['d'] = tmp_dice['e']
    dice['e'] = tmp_dice['b']
    dice['f'] = tmp_dice['d']
    #print(graph,dice)
    print(dice['b'])
    return dice

def method_3(dice):
    tmp_dice = dice.copy()
    dice['a'] = tmp_dice['b']
    dice['c'] = tmp_dice['d']
    dice['b'] = tmp_dice['c']
    dice['d'] = tmp_dice['a']
    dice['e'] = tmp_dice['e']
    dice['f'] = tmp_dice['f']
    print(dice['b'])
    return dice

def method_4(dice):
    tmp_dice = dice.copy()
    dice['a'] = tmp_dice['d']
    dice['c'] = tmp_dice['b']
    dice['b'] = tmp_dice['a']
    dice['d'] = tmp_dice['c']
    dice['e'] = tmp_dice['e']
    dice['f'] = tmp_dice['f']
    print(dice['b'])
    return dice

graph = [list(map(int,input().split())) for _ in range(N)]
command_list = input().split()

for command in command_list:
    if command=='1':
        if (y+1>=0 and y+1<M): 
            y+=1
            #print(x,y)
            if graph[x][y] == '0' or graph[x][y]==0:
                method_1(dice)
                graph[x][y] = dice['d']
            else:
                method_1(dice)
                dice['d'] = int(graph[x][y])
                graph[x][y] = 0
        else:
            continue
    if command=='2':
        if (y-1>=0 and y-1<M):
            y-=1
            #print(x,y)
            if graph[x][y] == '0' or graph[x][y] == 0:
                method_2(dice)
                graph[x][y] = dice['d']
            else:
                method_2(dice)
                #print(dice['d'], graph[x][y])
                dice['d'] = int(graph[x][y])
                graph[x][y] = 0
        else:
            continue
    if command=='3':
        if (x-1>=0 and x-1<N):
            x-=1
            #print(x,y)
            if graph[x][y] == '0' or graph[x][y]==0:
                method_3(dice)
                graph[x][y] = dice['d']
            else:
                method_3(dice)
                dice['d'] = int(graph[x][y])
                graph[x][y] = 0
    if command=='4':
        if (x+1>=0 and x+1<N):
            x+=1 
            #print(x,y)
            if graph[x][y] == '0' or graph[x][y]==0:
                method_4(dice)
                graph[x][y] = dice['d']
            else:
                method_4(dice)
                dice['d'] = int(graph[x][y])
                graph[x][y] = 0
