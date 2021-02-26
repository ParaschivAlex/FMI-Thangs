s="Maine plec sa car lemne. Ce tare. Bag pla. in viata mea"
lst=[]
s.split(".")
print(s)
lg=len(s)
p=0
for i in range (lg):
    if (i != lg - 1):
        if(s[i]=="." and s[i+2].isupper()):
            lst.append(s[p:i+1])
            p=i+1
    else:
        lst.append(s[p:i+1])
print(lst)