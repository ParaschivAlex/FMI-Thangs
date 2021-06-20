"""
Sortez muchiile crescator dupa greutate.
Parcurg muchiile sortate si caut 2 noduri care au muchie intre ele. Daca nodurile sunt deja unificate (fac parte din acelasi grup)
atunci nu include muchia. Altfel, o includem si le unificam.
Algoritmul se termina cand fiecare muchie a fost procesata sau toate varfurile au fost unificate.
"""

graph = [(0, 5, 3), (0, 1, 1), (0, 6, 3), (1, 6, 5), (1, 5, 4), (1, 2, 1), (6, 2, 3), (6, 7, 3), (5, 2, 1), (5, 35, 3), (2, 3, 1), (1,2,1), (2,7,1),(7,3,3)]

N = 7  # nr varfuri
M = len(graph)  # nr muchii
print("Muchii", M)

costAPM = 0
CC = [0 for _ in range(N)]  # vector de componente conexe
S = [0 for _ in range(M)]  # marcheaza muchiile selectate din APM


# def kruskal():
#     global costAPM
#     graph.sort(key=lambda x: x[2])  # sortez crescator dupa cost
#     for i in range(N):
#         CC[i] = i
#     k = 1
#     for p in range(N - 1):
#         while CC[graph[k][0]] == CC[graph[k][1]]:  # cautam o muchie in CC diferita
#             k += 1
#         S[k] = 1  # marcam selectarea muchiei k in APM
#         costAPM += graph[k][2]
#         ccfr = CC[graph[k][0]]  # unificam CC ale nodurile from si to
#         ccto = CC[graph[k][1]]
#         for i in range(N):
#             if CC[i] == ccto:
#                 CC[i] = ccfr

def kruskal():
    global costAPM
    graph.sort(key=lambda x: x[2])  # sortez crescator dupa cost
    for i in range(N):
        CC[i] = i
    for i in range(M):
        if CC[graph[i][0]] != CC[graph[i][1]]:
            S[i] = 1  # marcam selectarea muchiei k in APM
            costAPM += graph[i][2]
            ccfr = CC[graph[i][0]]  # unificam CC ale nodurile from si to
            ccto = CC[graph[i][1]]
            for j in range(N):
                if CC[j] == ccto:
                    CC[j] = ccfr


def afis():
    print("Costul este", costAPM)
    for i in range(M):
        if S[i] == 1:
            print(graph[i][0], graph[i][1])


kruskal()
afis()
