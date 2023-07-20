k = int(input())
for _ in range(k):
    inPut = input()
    stack = []
    for i in range(len(inPut)):
        if inPut[i] == '(':
            stack.append(inPut[i])
        if inPut[i] == ')':
            if stack:
                stack.pop()
            elif not stack:
                stack.append(')')
                break
            else:
                stack.pop()
    if not stack:
        print('YES')
    else:
        print('NO')