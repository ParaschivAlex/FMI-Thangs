# Sortarea topologica returneaza o ordonare a nodurilor in asa fel incat niciun nod din lista nu are muchie catre
# un nod care e inaintea lui in lista. Sortarea Topologica merge doar pe grafuri aciclice orientate (DAG - directed acyclic graph)

#Pentru fiecare nod i care are muchie care alt nod j, gasim i inainte lui j in lista din sortarea topologica.
graph = [[2],
         [0, 2, 4],
         [5, 6],
         [4, 6],
         [2],
         [],
         [5]]
print(len(graph))


def sortare_topologica(graph):
    N = 7  # numarul de noduri
    V = [False for _ in range(7)]  # vectorul de vizitati
    ordering = [0 for _ in range(7)]
    i = N - 1  # indexul pt ordering

    for k in range(N):
        if V[k] == False:
            visitedNodes = []
            i = dfs(i, k, V, ordering, graph)
            # for nod in visitedNodes:
            # ordering[i] = nod
            # i -= 1
    return ordering


def dfs(i, k, V, ordering, graph):
    V[k] = True

    for edge in graph[k]:
        print(edge, V[edge], graph[k])
        if V[edge] == False:
            i = dfs(i, edge, V, ordering, graph)
    # visitedNodes.append(k)
    ordering[i] = k
    return i - 1


sortare = sortare_topologica(graph)
for i in range(len(graph)):
    sortare[i] += 1
print(sortare)
