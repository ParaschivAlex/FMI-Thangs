s=(input("sir_1"))
oglindit=s[-1::-1]

def op(sir1,sir2):
    if(sir1[len(sir1)-1]!=sir2[0]):
        return (sir1+sir2)
    else:
        sirf=""
        for ch in sir1:
            if (ch in sir2):
                pass
            else:
                sirf+=ch
        for ch in sir2:
            if (ch in sir1):
                pass
            else:
                sirf+=ch
    return sirf

print (op(s,oglindit),op(oglindit,s))
if (len(op(s,oglindit))>len(op(oglindit,s))):
    print (op(s,oglindit))
else:
    print (op(oglindit,s))
