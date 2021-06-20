"""
id = 0
graph = [[1, 2],
         [0, 2],
         [0, 1, 3, 5],
         [2, 4],
         [3],
         [2, 6, 8],
         [5, 7],
         [6, 8],
         [5, 7]]
N = len(graph)

ids = [0 for _ in range(N)]
low = [0 for _ in range(N)]
visited = [False for _ in range(N)]
isArt = [False for _ in range(N)]
outEdgeCount = 0


def findArticulationPoints():
    bridges = []
    # Caut toate podurile din graf prin componentele conectate
    for i in range(N):
        if visited[i] == False:
            outEdgeCount = 0
            dfs(i, i, -1)
            isArt[i] = (outEdgeCount > 1)
    return isArt


def dfs(root, at, parent):
    global id, low, outEdgeCount, isArt
    if parent == root:
        outEdgeCount += 1
    visited[at] = True
    id += 1
    low[at] = ids[at] = id

    # Pentru fiecare muchie de la nodul 'at' la nodul 'to'
    for to in graph[at]:
        if to == parent:
            continue
        if visited[to] == False:
            dfs(root, to, at)
            low[at] = min(low[at], low[to])
            if ids[at] < low[to]:
                isArt[at] = True
            if ids[at] == low[to]:
                isArt[at] = True
        else:
            low[at] = min(low[at], ids[to])


print(findArticulationPoints())

"""
id = 0
graph = [[1, 2],
         [0, 2],
         [0, 1, 3, 5],
         [2, 4],
         [3],
         [2, 6, 8],
         [5, 7],
         [6, 8],
         [5, 7]]
N = len(graph)

ids = [0 for _ in range(N)]
low = [0 for _ in range(N)]
visited = [False for _ in range(N)]


def findBridges():
    bridges = []
    # Caut toate podurile din graf prin componentele conectate
    for i in range(N):
        if visited[i] == False:
            dfs(i, -1, bridges)
    return bridges


# Fac DFS ca sa gasesc podurile.
# at = nodul curent, parent = nodul precedent.
# Lista de poduri este mereu de lungime para si indecsii (2*i, 2*i+1) formeaza un pod.
# De exemplu, nodurile (0,1) sunt un pod.
def dfs(at, parent, bridges):
    global id, low
    visited[at] = True
    id += 1
    low[at] = ids[at] = id

    # Pentru fiecare muchie de la nodul 'at' la nodul 'to'
    for to in graph[at]:
        if to == parent:
            continue
        if visited[to] == False:
            dfs(to, at, bridges)
            low[at] = min(low[at], low[to])
            if ids[at] < low[to]:
                bridges.append((at, to))
        else:
            low[at] = min(low[at], ids[to])


print(findBridges())
