import sys
stack = [0]
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = [-1] * N
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        B[stack.pop()] = A[i]
    stack.append(i)
print(*B)