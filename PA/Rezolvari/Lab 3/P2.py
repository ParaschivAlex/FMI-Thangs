prop=input("propozitia este ")

lst2=[]
print(prop)
lst=prop.split()
print(lst)
d={}
minim=0
maxim=100
for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in lst:
    if minim<d[i]:
        minim=d[i]
    elif maxim>d[i]:
        maxim=d[i]

print(minim)
print(maxim)

for i in lst:
    if d[i]==maxim:
        lst2.append(i)
    elif d[i]==minim:
        lst2.append(i)
    else:
        continue
sorted(lst2)

print(lst2)


