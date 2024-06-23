N = int(input())
result = 0

for _ in range(N):
    word = input()
    grouped = []
    tmp =''
    for k in word:
        #print(k)
        if k in grouped and k!=tmp:
            #print(grouped)
            result += 1
            break
        else:
            grouped.append(k)
            tmp = k

print(N-result)