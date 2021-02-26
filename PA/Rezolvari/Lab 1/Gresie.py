L_1=int(input("Lungime bucatarie"))
L_2=int(input("Latime bucatarie"))
Arie=L_1*L_2
while(L_2!=0):
    r=L_1%L_2
    L_1=L_2
    L_2=r
Nr=Arie//L_1
Nr//=L_1
print(Nr,L_1)