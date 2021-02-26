f = open('regine.txt', 'r')
n = int(f.readline())
X = [0 for i in range(n+1)]
def verifica_coloana(X, k):
    for i in range(k):
        if X[k] == X[i]:
            return 0
    return 1

def verifica_diagonala(X, k):
    for i in range(k):
        if abs(X[k]-X[i]) == abs(k-i):
            return 0
    return 1

def afisare(X):
    print("Solutie: ")
    for i in range(1, n+1):
        for j in range(1, n+1):
            if X[i] == j:
                print("D ", end = '')
            else:
                print("_ ", end = '')
        print("\n")
    print("\n")

def bkt(k):
    global X, n
    for v in range(1, n+1):
        X[k] = v
        if verifica_coloana(X, k) and verifica_diagonala(X, k):
            if k == n:
                afisare(X)
            else:
                bkt(k+1)

bkt(1)

f.close()