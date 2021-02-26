x=int(input("lungima saritura initiala"))
n=int(input("numar sarituri pana scade"))
p=int(input("cu cate procente scade"))
m=int(input("numar sarituri totale"))
s=0
for i in range (m):
    s+=x
    if i+1 == n:
        k=p*x//100
        x-=k
        n*=2
print(s)
