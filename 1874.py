n = int(input())
flag = 1
stack = []
result = []
num = 1
for i in range(n):
    inPut = int(input())
    while num <= inPut:
        stack.append(num)
        result.append("+")
        num += 1

    if stack[-1] == inPut:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag = 0
        break

if flag == 1:
    for i in result:
        print(i)