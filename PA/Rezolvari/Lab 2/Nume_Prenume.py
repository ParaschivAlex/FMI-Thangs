s="Paraschiv Alexandru-Andrei"
crt=0
nume=0
poz=0
i=0
lg=len(s)
for i in range (lg):
    if (i==0 or s[i-1]==" " or s[i-1]=="-"):
        if s[i].islower():
            print("Nume gresit")
            break
    if s[i]=="-":
        crt+=1
        if crt>1:
            print("Nume gresit")
            break
    if s[i]=="-" or s[i]==" ":
        if i-poz+1<3:
            print("Nume gresit")
            break
        poz=i
    if s[i].isdigit():
        print("Nume gresit")
        break
    if s[i]==" " or s[i]=="-":
        nume+=1
        if nume>4:
            print("Nume gresit")
            break
    # print(crt)
else:
    print("Nume corect")
