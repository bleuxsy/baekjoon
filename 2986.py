N = int(input())
i = 2
count = 1
while i * i <= N:
    if N % i == 0:
        count = N // i
        break
    i += 1
print(N - count)
# count = 0
# for i in reversed(range(1, N)):
#     if N % i == 0:
#         break
# print(N-i)
