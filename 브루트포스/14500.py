# 테트로미노
# https://www.acmicpc.net/board/view/32956

col, row = map(int, input().split())
paper = []

for _ in range(col):
    paper.append(list(map(int, input().split())))

# 각 테트로미노는 2차원 배열이다.

class tetromino:
    def __init__(self):
        self.A = [[0,1,2,3]]
        self.B = [[0,1],[0,1]]
        self.C = [[0],[0],[0,1]]
        self.D = [[0],[0,1],[1]]
        self.E = [[0,1,2],[1]]
        self.A1 = [[0],[0],[0],[0]]

        self.C1 = [[2],[0,1,2]]
        self.C2 = [[0,1],[1],[1]]
        self.C3 = [[0,1,2],[0]]
        self.C4 = [[1],[1],[0,1]]
        self.C5 = [[0,1],[0],[0]]
        self.C6 = [[0],[0,1,2]]
        self.C7 = [[0,1,2],[2]]

        self.D1 = [[1,2],[0,1]]
        self.D2 = [[1],[1,0],[0]]
        self.D3 = [[0,1],[1,2]]

        self.E1 = [[0],[0,1],[0]]
        self.E2 = [[1],[0,1,2]]
        self.E3 = [[1],[0,1],[1]]
        self.tets = [self.A, self.B, self.C, self.D, self.E,
                     self.A1, self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7,
                     self.D1, self.D2, self.D3, self.E1, self.E2, self.E3]


tet = tetromino()
cnt_list = []
for i in range(col):
    for j in range(row):
        for t in tet.tets:
            if (len(t)+i)>col:
                continue
            if (max(map(max, t))+j)>=row:
                continue
            # 지금 위에서 t들이 끊기는 상태임.
            #print('coming')
            cnt = 0
            for x in range(len(t)):
                for y in t[x]:
                    cnt += paper[x+i][y+j]
            cnt_list.append(cnt)

print(max(cnt_list))