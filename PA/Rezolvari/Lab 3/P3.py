prop = input("textul: ")
d = {}
for i in prop:
    if d.get(i) != None:
        d[i] += 1
    else:
        d[i] = 1
print(d)
