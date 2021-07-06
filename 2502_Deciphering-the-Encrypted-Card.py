while True:
    try:
        C, N = map(int, input().split())
        chiper_1 = input().lower()
        chiper_2 = input().lower()
        chiper_1_u = chiper_1.upper()
        chiper_2_u = chiper_2.upper()
        output = ''
        for i in range(N):
            word = input()
            word = list(word)

            for j in range(len(word)):
                for k in range(C):
                    if word[j] == chiper_1[k]:
                        word[j] = chiper_2[k]
                    elif word[j] == chiper_2[k]:
                        word[j] = chiper_1[k]
                    elif word[j] == chiper_1_u[k]:
                        word[j] = chiper_2_u[k]
                    elif word[j] == chiper_2_u[k]:
                        word[j] = chiper_1_u[k]
                output += word[j]
            print(output)
            output = ''
        print()
    except:
        break

#Another way:
'''
while True:
    try:
        C, N = input().split()
        C = int(C)
        N = int(N)
        word1 = list(map(str, input().lower()))[:C]
        word2 = list(map(str, input().lower()))[:C]
        ans = ""
        for i in range(N):
            word = input()
            for j in range(len(word)):
                if word[j].lower() in word1:
                    for x in range(len(word1)):
                        if word[j].lower() == word1[x]:
                            ans += word2[x]
                elif word[j].lower() in word2:
                    for x in range(len(word2)):
                        if word[j].lower() == word2[x]:
                            ans += word1[x]
                else:
                    ans += word[j].lower()
            if word[0].isupper():
                print(ans.capitalize())
                ans=""
            else:
                print(ans)
                ans = ""
        print()
    except:
        break
'''