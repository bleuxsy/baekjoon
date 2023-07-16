N = list(input())
print(N)
N.sort()
result = [0]*10

for i in N:
    if i == "9" or i == "6":
        if result[6] == result[9]:
            result[6] += 1
        else:
            result[9] += 1

    else:
        result[int(i)] += 1
print(max(result))









