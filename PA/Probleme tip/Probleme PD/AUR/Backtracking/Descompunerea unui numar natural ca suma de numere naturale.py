f = open('descompunere.txt', 'r')
n = int(f.readline())
X = [0 for i in range(n+1)]
def afisare(X, n):
    print("%s = " % n, end = '')
    for i in range(len(X)):
        if i == len(X)-1:
            print(X[i])
        else:
            print("%s + " % X[i], end = '')

def bkt(k):
    global X, n
    for v in range(1, n-k+2):
        X[k] = v
        suma = sum(X[:k+1])
        if suma <= n:
            if suma == n:
                afisare(X[:k+1], n)
            else:
                bkt(k+1)

bkt(0)

f.close()