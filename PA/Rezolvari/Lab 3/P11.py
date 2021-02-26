lista_poz=[]
N=5
def dreapta(i,j):
    if (j!=N-1):
        misc=0
        while (((i,j+1)not in lista_poz or (i,j+1) in lista_poz and lista_poz[lista_poz.index((i,j+1))][0]!=i and lista_poz[lista_poz.index((i,j+1))][1]!=j) and j!=N-1):
            j+=1
            lista_poz.append((i,j))
            misc+=1
        return [misc,i,j]
    return [0,i,j]
def jos(i,j):
    if (i!=N-1):
        misc=0
        while (((i+1,j) not in lista_poz or (i,j+1) in lista_poz and lista_poz[lista_poz.index((i,j+1))][0]!=i and lista_poz[lista_poz.index((i,j+1))][1]!=j) and i!=N-1):
            i+=1
            lista_poz.append(((i,j)))
            misc+=1
        return  [misc,i,j]
    return [0,i,j]
def stanga(i,j):
    if(j!=0):
        misc=0
        while(((i,j-1)not in lista_poz or (i,j+1) in lista_poz and lista_poz[lista_poz.index((i,j+1))][0]!=i and lista_poz[lista_poz.index((i,j+1))][1]!=j) and j!=0):
            j-=1
            lista_poz.append((i,j))
            misc+=1
        return  [misc,i,j]
    return [0,i,j]
def sus(i,j):
    if (i!=0):
        misc=0
        while (((i-1,j) not in lista_poz or (i,j+1) in lista_poz and lista_poz[lista_poz.index((i,j+1))][0]!=i and lista_poz[lista_poz.index((i,j+1))][1]!=j) and i!=0):
            i -=1
            lista_poz.append((i, j))
            misc+=1
        return [misc,i,j]
    return [0,i,j]
matrice=[]
for i in range(N):
    a=[]
    for j in range (N):
        a.append((i)*5+j+1)
    matrice.append(a)
for i in range(N):
    for j in range (N):
        print(matrice[i][j],end=' ')
    print()
a=0
b=0
nr=0
k=0
lista_poz.append((0,0))
while (nr<N*N):
    l=dreapta(a,b)
    k=l[0]
    a=l[1]
    b=l[2]
    del l
    l=[]
    nr+=k
    l=jos(a,b)
    k = l[0]
    a = l[1]
    b = l[2]
    print (a,b)
    del l
    l = []
    nr+=k
    l=stanga(a,b)
    k = l[0]
    a = l[1]
    b = l[2]
    del l
    l = []
    nr+=k
    l=sus(a,b)
    k = l[0]
    a = l[1]
    b = l[2]
    del l
    l = []
    nr+=k
print(lista_poz)