import math
f=open("triplete_pitagorice.txt", "w+")
c=0
def ipotenuza (a,b):
    c=math.sqrt((a**2)+(b**2))
    return c
#a=int(input("a="))
b=int(input("b="))
#print(ipotenuza(a,b))
for a in range (1,b+1,1):
    x=ipotenuza(a,b)
    if x == int(x):
        #print(a, ", ", b,", ", x)
        f.write(str(a))
        f.write(" ")
        f.write(str(b))
        f.write(" ")
        f.write(str(x))
        f.write("\n")
f.close()

#terminat