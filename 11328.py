N = int(input())
for _ in range(N):
    word1, word2 = map(str,input().split())
    word1 = list(word1)
    word2 = list(word2)
    word1.sort()
    word2.sort()
    if len(word1) != len(word2):
        print("Impossible")
        continue

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            flag = "Impossible"
            break;
        else:
            flag = "Possible"
    print(flag)





