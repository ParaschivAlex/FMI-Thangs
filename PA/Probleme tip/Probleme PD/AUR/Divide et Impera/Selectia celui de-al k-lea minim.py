f = open('kthmin.txt', 'r') # 12:22:15
k = int(f.readline())
v = [int(i) for i in f.readline().split()]
def pivot(A):
    if len(A) <= 5:
        return sorted(A)[len(A)//2]
    else:
        subliste = [sorted(A)[i:i+5] for i in range(0, len(A), 5)]
        mediane = [s1[len(s1)//2] for s1 in subliste]
        return pivot(mediane)

def quickselect(A, k, f_pivot = pivot):
    pivot = f_pivot(A)
    L = [x for x in A if x < pivot]
    E = [x for x in A if x == pivot]
    G = [x for x in A if x > pivot]
    if k < len(L):
        return quickselect(L, k, f_pivot)
    if k < len(L) + len(E):
        return E[0]
    else:
        return quickselect(G, k-len(L)-len(E), f_pivot)

print(quickselect(v, k))