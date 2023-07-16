S=input()
alphabet=[0]*26
for i in S :
    alphabet[ord(i)-97]+=1
print(*alphabet)