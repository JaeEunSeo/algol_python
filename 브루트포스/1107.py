numbers = ['0','1','2','3','4','5','6','7','8','9']

N = int(input())
M = int(input())

flag = True if M==0 else False

def jump():
        count = [abs(100-N)]
        for i in range(1000000):
            for j in str(i):
                if j in broken:
                    break
            else:
                count.append(len(str(i))+abs(N-i))
        return min(count)
    
# 고장난 버튼이 없을 경우
if flag:
    print(min(len(str(N)), abs(N-100)))

if not flag:
    broken = list(map(str,input().split()))
    if len(broken)>0:   
        [numbers.remove(n) for n in broken]

    if N == 100:
        ans = 0
    elif M==10:
        ans = abs(N-100)
    else:
        ans = jump()

    print(ans)