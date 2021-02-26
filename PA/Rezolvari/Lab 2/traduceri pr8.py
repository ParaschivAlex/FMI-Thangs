# A). i).
# s=input("sirul")
# n=""
# lg=len(s)
# for i in range (lg):
#     if s[i] in "aeiouAEIOU":
#         n+=s[i]+"p"+s[i]
#     else:
#         n+=s[i]
#
# print(n)


# A). ii).
# s = input("sirul")
# n = ""
# i=0
# lg = len(s)
# while i < lg:
#     if s[i] == "p":
#         if s[i - 1] in "aeiouAEIUO" and s[i + 1] in "aeiouAEIUO":
#             i+=1
#     else:
#         n += s[i]
#     i+=1
# print(n)

# B).
sir="A-na a-re mul-te me-re ro-sii si de-li-cioa-se."
sir2=""
i=0
while (i<len(sir)):
    if (i!=len(sir)-1):
        if(sir[i+1]=="-" or sir[i+1]==" " or i==len(sir)-2):
            sir2+=sir[i]+"p"+sir[i].lower()
        else:
            sir2+=sir[i]
    i+=1
print(sir2)
print(sir2.replace("-",""))
i=0
while (i<len(sir2)):
    if (sir2[i]!="-"):
        print(sir2[i],end="")
    i+=1
