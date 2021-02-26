sir= "Langa o cabana, stand pe o banca, un bacan a spus un banc bun."
cuv="bacan"
alfabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ok=0
lg=len(sir)
for i in range (lg):
    if (i==0 or sir[i-1]==" "):
        k=i
    if (sir[i] not in alfabet):
        log=1
        j=k
        while (j<i):
            if (sir[j] not in cuv):
                log=0
            j+=1
        if (log==1):
            print(sir[k:i])
            ok=1
if (not ok):
    print("ghinion")
