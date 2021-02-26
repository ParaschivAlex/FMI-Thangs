import math
a=int(input("a = ?"))
b=int(input("b = ?"))
c=int(input("c = ?"))
d=b**2-4*a*c
if d < 0:
    d=-d
    m=-b/2*a
    n=math.sqrt(d)/2*a
    if n>=0:
        print(m, "+i", n)
    else:
        print(m,"-i",n)
elif d==0:
    print(-b/2*a)
else:
    d=math.sqrt(d)
    m=(-b+d)/2*a
    n=(-b-d)/2*a
    print(m, n)