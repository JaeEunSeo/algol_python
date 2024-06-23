N, C = map(int, input().split())
numbers = list(map(str, input().split()))

cnt=dict()

for n in numbers:
    if n in cnt.keys():
        cnt[n] +=1
    else:
        cnt[n] = 1

# dict를 value 순서대로 정렬하되, 들어온 순서는 지켜야 함. 
# dict를 앞에서부터 순회하며, pivot을 정의??
        
max = max(cnt.values())

for i in range(max, 0, -1):
    for k in cnt.keys():
        if cnt.get(k)==i:
            for _ in range(i):
                print(k, end=' ')
            
    