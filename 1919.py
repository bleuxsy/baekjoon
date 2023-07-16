LIST = [0]*26

for i in list(input()):
    LIST[ord(i)-97] += 1
for j in list(input()):
    LIST[ord(j)-97] -= 1
print(sum(map(abs, LIST)))




