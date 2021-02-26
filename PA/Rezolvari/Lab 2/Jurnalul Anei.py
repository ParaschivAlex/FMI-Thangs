s=input()
lg=len(s)
sum=0
i=0
while (i < lg):
    if (s[i].isdigit()==True):
        for j in range (i+1, lg, 1):
            if(s[j].isdigit()==False):
                sum += int(s[i:j])
                #print(s[i:j])
                i=j
                break
    i+=1

print(sum, "RON")