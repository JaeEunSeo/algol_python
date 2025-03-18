def binary(n):
    binary = ''
    tmp_n = n
    h = 0
    while tmp_n>0:
        binary = str(tmp_n % 2) + binary
        tmp_n = tmp_n // 2
    while len(binary)>2**h-1:
        h += 1
    binary = '0' * (1+2**h-1-len(binary)) + binary
    return binary    
    
def solution(numbers):
    answer= []
    ans = 1
    def dfs(bin_n, start, end):
        nonlocal ans  
        root = (start+end)//2
        left, right = start+(root-start)//2, end-(end-root)//2
        if root % 2 == 1:
            return 
        if bin_n[root] == '0' and (bin_n[left]=='1' or bin_n[right]=='1'):
            ans = 0
            return 
        dfs(bin_n, root+1, end)
        dfs(bin_n, start, root-1)
        return 

    for n in numbers:
        ans = 1
        bin_n = binary(n)

        dfs(bin_n, 1, len(bin_n)-1)
        answer.append(ans)
    
    return answer

print(solution([1,2,96]))