def solution(N, number):
    if N==number:
        return 1
    dp = [set() for _ in range(8)]

    for i in range(8):
        dp[i].add(int(str(N)*(i+1)))

    for i in range(8):
        new = dp[i]
        for j in range(i):
            for p1 in dp[j]:
                for p2 in dp[i-j-1]:
                    new.add(p1+p2)
                    new.add(p1*p2)
                    new.add(p1-p2)
                    if p2!=0:
                        new.add(p1//p2)
        dp[i] = new
        if number in new:
            return i+1
        
    return -1
 
if __name__=='__main__':
    print(solution(4,31))