f=open ("cheltuieli.txt")
sir=f.read()
i=0
suma=0
while (i<len(sir)-4):
    if (i==0 or sir[i-1]==" "):
        k=i
    if (sir[i]==" "):
        if ('.' not in sir[k:i]):
            if (sir[k:i].isdecimal()):
                if (sir[i+1:i+4]=="RON"):
                    suma+=int(sir[k:i])
        else:
            x=sir[k:i].split(".")
            if (x[0].isdecimal() and x[1].isdecimal()):
                if (sir[i+1:i+4]=="RON"):
                    suma+=float(sir[k:i])
    i+=1
print (suma)