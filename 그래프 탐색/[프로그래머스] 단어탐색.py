def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    def dfs(cnt, s):
        if cnt == 5:
            return
        for w in words:
            dictionary.append(s + w)
            dfs(cnt+1, s+w)
    dfs(0,'')
    return dictionary.index(word)+1