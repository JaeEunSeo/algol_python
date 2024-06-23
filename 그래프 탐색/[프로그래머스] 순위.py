class node:
    def __init__(self, x):
        self.x = x
        self.win = []
        self.lose = []

def dfs_win(player, visited, cnt):
    # 매개변수 : node
    # winner 개수 count
    for n in player.win:
        if visited[n.x] == 0:
            visited[n.x] = 1
            cnt += 1
            cnt = dfs_win(n, visited, cnt)
    return cnt
            
def dfs_lose(player, visited, cnt):
    # 매개변수 : node
    for n in player.lose:
        if visited[n.x] == 0:
            visited[n.x] = 1
            cnt += 1
            cnt = dfs_lose(n, visited, cnt)
    return cnt
            
        
def solution(n, results):
    players = [node(i) for i in range(n+1)]
    answer = 0
    for i in range(len(results)):
        a = int(results[i][0]); b = int(results[i][1])
        players[b].win.append(players[a])
        players[a].lose.append(players[b])
        
    for i in range(1,n+1):
        visited = [0 for _ in range(n+1)]; cnt = 0
        result = dfs_win(players[i], visited, cnt) + dfs_lose(players[i], visited, cnt)
        if result == n-1:
            answer += 1
    
    return answer