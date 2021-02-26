n=int(input("care este numarul de valori dorite?"))
max1, max2=0,0
for i in range (n):
    x=int(input())
    if(x>max1):
        max2=max1
        max1=x
    elif(x<max1 and x >max2):
        max2=x
if max1!=0 and max2!=0:
    print(max1, " ", max2)
else:
    print("Imposibil")