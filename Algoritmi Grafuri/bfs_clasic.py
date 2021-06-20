# f = open("date.txt")
# n, m = int(f.readline.split())
# matrix = [[0 for _ in range(n)] for _ in range(n)]
# for _ in range (m):
# i,j = int(f.readline().split())
# matrix[i][j] = 1


matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
n = 4
coada = [0 for _ in range(n)]
viz = [0 for _ in range(n)]


def bfs(x):
    print(x)
    coada[0] = x
    p, u = 0, 0
    viz[x] = 1
    while p <= u:
        crt = coada[p]
        p += 1
        for i in range(n):
            if matrix[crt][i] == 1 and viz[i] == 0:
                u += 1
                coada[u] = i
                print(i)
                viz[i] = 1

def bfs2(x):
    print(x)
    coada.append(x)
    p, u = 0, 0
    viz[x] = 1
    while coada:
        crt = coada.pop(0)
        for i in range(n):
            if matrix[crt][i] == 1 and viz[i] == 0:
                coada.append(i)
                print(i)
                viz[i] = 1

# def reconstituire(start, final, prev):
    # cursul aluia de pe yt pt asta

# bfs(0)
bfs2(0)

