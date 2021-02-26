f = open('tms.txt', 'r')
n = int(f.readline())

v = [int(i) for i in f.readline().split()]

def suma(v):
    c = s = 0
    for nr in v:
        c += nr
        s += c
    return s
s = suma(v)/n

print("Timpul mediu de asteptare este %s. " % s)

v.sort()

s = suma(v)/n

print("Timpul minim de asteptare este %s. " % s)