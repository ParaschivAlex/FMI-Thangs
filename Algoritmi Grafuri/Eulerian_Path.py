# O(E) pentru drum Eulerian

"""
Drum EULERIAN = drum care parcurge toate muchiile din graf O SINGURA DATA.
"""

"""
Ai poza pentru cazurile de verificare cu un tabel.
"""

"""
Pentru a verifica ca exista un drum Eulerian:
Cel mult un varf are grad exterior - grad interior = 1 si
cel mult un varf are grad interior - grad exterior = 1 si
toate celelalte varfuri au grad interior = grad exterior
"""

"""
Incepem cu nodul care are  IN - OUT = 1 
si terminam cu nodul care are OUT - IN = 1.
Daca avem pt toate nodurile IN = OUT atunci incepem
cu oricare nod care are IN != 0 SI OUT != 0
"""

# ------------------------------------------------
"""
Idee:
Parcurgem cu DFS si cand ajungem la un nod care nu mai are muchii nevizitate ( OUT[i] == 0) 
atunci adaugam nodul respoectiv la solutii si revenim pana gasim un nod care mai are muchii nevizitate.
Cand revenim, daca nodul mai are muchii cautam in continuare cu dfs recursiv. 
"""

graph = [
    [],
    [2, 3],
    [2, 4, 4],
    [1, 2, 5],
    [3, 6],
    [6],
    [3]
]

N = len(graph)
M = 0
for muchii in graph:
    M += len(muchii)
# print(N, M)

nod_in = [0 for _ in range(N)]
nod_out = [0 for _ in range(N)]

path = []


def findEulerianPath():
    countInOutDegrees()
    if not graphHasEulerianPath():
        return None
    dfs(findStartNode())
    if len(path) == M + 1:
        return path
    return None


def countInOutDegrees():
    for i in range(N):
        for edge in graph[i]:
            nod_out[i] += 1
            nod_in[edge] += 1


def graphHasEulerianPath():
    start_nodes, end_nodes = 0, 0
    for i in range(N):
        if abs(nod_out[i] - nod_in[i]) > 1:
            return False
        elif nod_out[i] - nod_in[i] == 1:
            start_nodes += 1
        elif nod_in[i] - nod_out[i] == 1:
            end_nodes += 1
    return end_nodes == 0 and start_nodes == 0 or end_nodes == 1 and start_nodes == 1


def findStartNode():
    start = 0
    for i in range(N):
        if nod_out[i] - nod_in[i] == 1:  # nod unic de start
            return i
        if nod_out[i] > 0:  # incep la orice nod cu out > 0
            start = i
    return start


def dfs(at):
    while nod_out[at]:  # cat timp mai am muchii out din nod
        nod_out[at] -= 1
        next_edge = graph[at][nod_out[at]]  # selectam urmatoarea muchie nevizitata
        dfs(next_edge)
    path.append(at)  # adaug in solutie


solutie = findEulerianPath()
print(solutie)
