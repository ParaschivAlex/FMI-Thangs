m = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
]

n = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
count = 0
components = [0 for _ in range(len(n))]
viz = [0 for _ in range(len(n))]

def findComponents():
    global components, count
    for i in range(len(n)):
        if viz[i] == 0:
            count +=1
            dfs(i)
    return count, components

def dfs(x):
    print(x)
    viz[x] = 1
    components[x] = count
    for i in range(len(n)):
        if m[x][i] == 1 and viz[i] == 0:
            dfs(i)

numar, comp = findComponents()
print(numar, comp)