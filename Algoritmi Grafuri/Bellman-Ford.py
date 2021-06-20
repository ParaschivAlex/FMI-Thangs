# O(E*V) # edges * vertices
# si pentru costuri negative

graph = [(0, 1, 5),
         (1, 2, 20),
         (1, 5, 30),
         (1, 6, 60),
         (2, 3, 10),
         (2, 4, 75),
         (3, 2, -15),
         (4, 9, 100),
         (5, 4, 25),
         (5, 6, 5),
         (5, 8, 50),
         (6, 7, -50),
         (7, 8, -10)]

graph2 = [
    [(1, 4), (6, 2)],
    [(1, -1), (2, 3)],
    [(3, 3), (4, 1)],
    [(5, -2)],
    [(5, 2)],
    [],
    [(4, 2)]
]

print("N:", len(graph))
print("Graph:", graph)
N = 10
infinit = 999999999
minus_infinit = -infinit


def bellmanford(g, n, start):
    dist = [infinit for _ in range(N)]  # un vector cu distante de la nodul de start la oricare alt nod
    dist[start] = 0
    """Parcurg muchiile de n-1 ori si calculez costurile minime pt a ajunge in noduri. Vad daca este influentat direct sau indirect de vreun ciclu negativ"""
    for i in range(n - 1):
        for edge in g:
            if dist[edge[0]] + edge[2] < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
    """Daca e influentat modific lista de costuri dist."""
    for i in range(n - 1):
        for edge in g:
            if dist[edge[0]] + edge[2] < dist[edge[1]]:
                dist[edge[1]] = minus_infinit

    return dist


print(bellmanford(graph, N, 0))

""" 
# Credit Staicu:


class Edge:
    def __init__(self, fr, to, cost):
        self.fr = fr
        self.to = to
        self.cost = cost


def bellmanFord(g, v, start):
    
    # Parcurg toate muchiile din graf de v-1 ori (v = nr de noduri) de doua ori.
    # Prima data le parcurg pentru a calcula costurile minime pentru a ajunge in fiecare nod.
    # Iar a doua oara le parcurg pentru a vedea care cost se mai modifica. daca se modifica la a doua parcurgere,
    # inseamna ca acel nod e intr-un ciclu negativ, sau e afectat de un ciclu negativ din drumul sau.
    # Trebuie parcurse de v-1 ori toate muchiile grafului pentru a ne asigura ca se propaga in graf efectul ciclului
    # negativ si sa nu pierdem vreun nod care nu a apucat sa isi modifice costul din cauza acestuia.
    
    dist = [float('inf') for i in range(v)]
    dist[start] = 0

    for i in range(v - 1):
        for edge in g:
            if dist[edge.fr] + edge.cost < dist[edge.to]:
                dist[edge.to] = dist[edge.fr] + edge.cost

    for i in range(v - 1):
        for edge in g:
            if dist[edge.fr] + edge.cost < dist[edge.to]:
                dist[edge.to] = float('-inf')

    return dist


graph = [
    Edge(0, 1, 5),
    Edge(1, 2, 20),
    Edge(1, 5, 30),
    Edge(1, 6, 60),
    Edge(2, 3, 10),
    Edge(2, 4, 75),
    Edge(3, 2, -15),
    Edge(4, 9, 100),
    Edge(5, 4, 25),
    Edge(5, 6, 5),
    Edge(5, 8, 50),
    Edge(6, 7, -50),
    Edge(7, 8, -10),
]


print(bellmanFord(graph, 10, 0))"""
