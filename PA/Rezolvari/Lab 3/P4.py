d1={"mere":5,"pere":4,"rosii":3}
d2={"rosii":3,"castraveti":4,"broccoli":6}
d={}
for k,v in d1.items():
    if(d.get(k)==None):
        d[k]=d1[k]
    else:
        d[k]+=d1[k]
for k,v in d2.items():
    if (d.get(k) == None):
        d[k] = d2[k]
    else:
        d[k] += d2[k]
print (d)
