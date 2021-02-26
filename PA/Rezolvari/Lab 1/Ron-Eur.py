n=int(input("Numar zile"))
x=float(input("Prima zi"))
max=0
for i in range (1,n):
    y=float(input("Alta zi"))
    r=y-x
    if r > max:
        max=r
        z=i+1
    x=y
print(max)
print(z-1,z)