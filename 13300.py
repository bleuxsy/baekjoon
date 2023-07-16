N, K = map(int, input().split())
rows = 6
cols = 2
arr = [[0]*2 for _ in range(6)] #2차원배열

for i in range(N):
    S,Y = map(int,input().split())
    arr[Y-1][S-1] += 1

room=0
for i in range(rows):
    for j in range(cols):
        if (arr[i][j]%K == 0):
            room += arr[i][j]/K
        else:
            room += arr[i][j]//K + 1
print(int(room))

