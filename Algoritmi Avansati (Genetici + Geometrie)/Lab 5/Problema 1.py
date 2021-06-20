# Citirea din consola

xp = int(input("xP = "))
yp = int(input("yP = "))
xq = int(input("xQ = "))
yq = int(input("yQ = "))
xr = int(input("xR = "))
yr = int(input("yR = "))

# Calculare determinant, daca = 0 --> coliniare, > 0 --> viraj la stanga, < 0 --> viraj la dreapta

determinant = xq * yr + xp * yq + xr * yp - xq * yp - xr * yq - xp * yr

# Afisarea pe cazuri

if determinant > 0:
    print("Viraj la stanga!")
elif determinant < 0:
    print("Viraj la dreapta!")
else:
    print("Punctele sunt coliniare")

# Cazuri testate: (-1,1) (0,1) (2,1) coliniare
# (-2,4) (-1,1) (0,1) viraj la stanga
# (1,-1) (3,3) (5,-5) viraj la dreapta
print(determinant)
