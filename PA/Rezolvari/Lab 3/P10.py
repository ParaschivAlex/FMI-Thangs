l=[]
i=0
while (1):
    scor=int(input())
    if (scor==-1):
        break
    i+=1
    nume=input()
    t=(scor,nume,i)
    l.append(t)
print(l)
s=set()
for k in l:
    s.add(k[0])
print(s)
d={}
for k in l:
    if (d.get(k[0])==None):
        d[k[0]]=[]
        d[k[0]].append((k[1],k[2]))
    else:
        d[k[0]].append((k[1],k[2]))
print (d)