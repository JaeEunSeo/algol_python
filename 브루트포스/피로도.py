def solution(k, dungeons):
    def dfs(k, cnt, dungeons):
        max_cnt = cnt

        for j in range(len(dungeons)):
            if dungeons[j][0]>k:
                continue
            
            tmp_dungeons = dungeons[:j]+dungeons[j+1:]
            
            max_cnt = max(max_cnt, dfs(k-dungeons[j][1], cnt+1, tmp_dungeons))
        return max_cnt
    
    return dfs(k, 0, dungeons)