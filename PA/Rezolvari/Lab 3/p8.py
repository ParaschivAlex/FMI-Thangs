f = open("inventar.txt")
d = {}
sir = f.readline()
i = 0
k = 0
while (sir):
    i = 0
    sirc = ""
    sact = set()
    log = 1
    while (log == 1):
        if (sir[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&"):
            pass
        else:
            sirc = sir[0:i]
            log = 0
        i += 1
    while (i < len(sir)):
        if (sir[i].isdecimal() and not sir[i - 1].isdecimal()):
            k = i
        if (sir[i] == " " or i == len(sir) - 1):
            if (k != i):
                sact.add(sir[k:i])

            else:
                sact.add(sir[k:i + 1])

        i += 1
    d[sirc] = sact
    sir = f.readline()
print(d)

setintersectie = set()
for k in d.values():
    if (len(setintersectie) == 0):
        setintersectie = k
    else:
        setintersectie = setintersectie and k  # sau setintersectie&k
print("intersectia este ", setintersectie)

# setreuniune = set()
# for k in d.values():
#     setintersectie += d[k]  # sau setreuniune|k
# print("reuniunea este ", setreuniune)
# CARE ESTE REUNIUNEA???#

for k1,v1 in d.items():
    s=v1
    for k2,v2 in d.items():
        if (k1!=k2):
            s=s-v2
    print(k1,s,end=' ')