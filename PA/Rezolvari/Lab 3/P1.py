v=[]
# t=(10, 7, 5, 3, 2)
n=int(input("n= "))
for i in range (n):
    v.append(int(input("valoare")))

sorted(v, reverse=True)
#aux=sorted(t, reverse=True)
#print(aux)
print(v[0])
max=v[0]
for i in v:
    if i!=max:
        print(i)
        break

