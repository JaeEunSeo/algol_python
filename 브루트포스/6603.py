def dfs(cur):
    global arr
    if len(arr)==6:
        for _ in arr:
            print(_, end=' ')
        print('')
        return
    for j in range(cur, num):
        arr.append(lst[j])
        dfs(j+1)
        arr.remove(lst[j])
    
    return

while True:
    numbers = input()
    if numbers == '0':
        exit()
    numbers = list(map(int, numbers.split()))
    arr = []
    num = numbers[0]
    lst = numbers[1:]
    dfs(0)
    print(end='\n')