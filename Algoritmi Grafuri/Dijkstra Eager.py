# doar costuri pozitive
# O(E*log(V))

import operator
from collections import OrderedDict

graph = [
    [(1, 5), (2, 1)],
    [(2, 2), (3, 3), (4, 20)],
    [(1, 3), (4, 12)],
    [(2, 3), (4, 2), (5, 6)],
    [(5, 1)],
    []
]
print("N:", len(graph))
print("Graph:", graph)
N = len(graph)
infinit = 99999999


def check(x, lst):
    for i in range(len(lst)):
        if lst[i][0] == x:
            return 1
    return 0


def dijkstra(g, n, start):
    vis = [False for _ in range(n)]
    prev = [None for _ in range(n)]
    dist = [infinit for _ in range(n)]  # am presupus ca 99999999 == infinit
    dist[start] = 0  # distanta pentru nodul de start este 0
    pq = []  # un indexed priority queue heap
    pq.append([start, 0])  # adaug in indexed priority queue heap perechea (start, 0)
    while len(pq):  # cat timp pq nu este vida
        print(pq)
        index, val_min = pq.pop(0)  # extrag din pq
        print(pq)
        vis[index] = True  # marchez ca am vizitat
        if dist[index] < val_min:  # ignor perechile din pq pentru care am gasit deja o ruta mai buna
            continue
        for edge in g[index]:  # pentru muchie in lista de muchii
            if vis[edge[0]]:  # daca nodul la care se ajunge este deja vizitat continui
                continue
            newcost = dist[index] + edge[1]  # altfel noua distanta devine ce am pana acolo + costul
            if newcost < dist[edge[0]]:
                dist[edge[0]] = newcost
                if check(edge[0], pq) == 0:  # daca nodul nu este in indexed pq
                    pq.append([edge[0], newcost])  # il adaug
                else:  # altfel ii updatez costul nou
                    for idx in range(len(pq)):
                        if pq[idx][0] == edge[0]:
                            pq[idx][1] = newcost
                pq.sort(key=lambda x: x[1]) # sortez dupa cost
                prev[edge[0]] = index # adaug in vectorul de tati
    return dist, prev


def findShortestPath(g, n, start, end):
    global infinit, N
    dist, prev = dijkstra(g, n, start)
    path = []
    i = end
    print("Dist:", dist, '\n', "Prev:", prev)
    if dist[end] == infinit:
        return path
    else:
        while i is not None:
            path.append(i)
            i = prev[i]
    path.reverse()
    return path


print(findShortestPath(graph, N, 0, 5))
