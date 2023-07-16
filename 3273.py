n = int(input())
N = list(map(int, input().split()))
N.sort()
x = int(input())
i = 0
j = (int(n)-1)
count = 0
while i < j:
    sum = N[i] + N[j]
    if sum == x:
        count += 1
    if sum < x:
        i += 1
        continue
    j -= 1
print(count)