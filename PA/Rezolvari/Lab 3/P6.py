sir = "mere pere droguri mofturi CamIoane"
rime = {}
for i in range(len(sir)):
    if (i == 0 or sir[i - 1] == " "):
        k = i
    if (sir[i] == " "):
        if (rime.get(sir[i - 2:i]) == None):
            rime[sir[i - 2:i]] = [sir[k:i]]
        else:
            rime[sir[i - 2:i]].append(sir[k:i])
    if (i == len(sir) - 1):
        if (rime.get(sir[i - 1:i + 1]) == None):
            rime[sir[i - 1:i + 1]] = [sir[k:i + 1]]
        else:
            rime[sir[i - 1:i + 1]].append(sir[k:i + 1])
final = {}
print(rime)
for j, v in rime.items():
    if (len(rime[j]) >= 2):
        final[j] = v
print(final)
