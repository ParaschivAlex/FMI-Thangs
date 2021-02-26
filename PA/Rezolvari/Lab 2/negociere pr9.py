sir = "Eu am de gând să vând vaza aceasta pentru $5. Ce plăcut, chiar mi-ar plăcea să o achiziționez,doar că am numai $3 la mine. Este suficient? Nu, insist să obțin 5$ pe ea. Bine, atunci voi scoate niște bani și-ți aduc cei  $5."
valf1, valf2 = "", ""
i = 0
schimb = 1
nr = 0
while (i < len(sir)):
    if (sir[i].isdigit()):
        k = i
        nr += 1
        while (sir[i].isdigit()):
            i += 1
            l = i
        if (schimb == 1):
            valf1 = int(sir[k:i])
            schimb = 0
        else:
            valf2 = int(sir[k:i])
            schimb = 1
    if (nr == 2 and i == l):
        print(valf1, valf2)
    i += 1
print(valf1, valf2)
if (valf1 == valf2):
    print("s-au inteles")
else:
    print("nu s-au inteles")
