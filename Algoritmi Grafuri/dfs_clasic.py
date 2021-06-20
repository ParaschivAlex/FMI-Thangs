#f = open("date.txt")
#n, m = int(f.readline.split())
#matrix = [[0 for _ in range(n)] for _ in range(n)]
#for _ in range (m):
    #i,j = int(f.readline().split())
    #matrix[i][j] = 1


matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
n = 4
viz = [0 for _ in range(n)]

def dfs(x):
    print(x)
    viz[x] = 1
    for i in range (n):
        if matrix[x][i] == 1 and viz[i] == 0:
            dfs(i)

dfs(0)