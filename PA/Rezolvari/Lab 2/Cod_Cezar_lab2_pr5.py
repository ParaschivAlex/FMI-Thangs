s=input()
k=int(input())
sn=""
for ch in s:
    if ch.isupper():
        sn+=chr((ord(ch)+k-ord('A'))%26+ord('A'))
    else:
        sn+=chr((ord(ch)+k-ord('a'))%26+ord('a'))
print(sn)