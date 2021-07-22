x = 1
while True:
    n = int(input())
    if n == 0:
        break
    inp = input()
    if n == 1:
        print("Teste {}\n{}\n".format(x, inp))
        x += 1
    else:
        sign = []
        numbers = []
        a = 0
        for i in range(len(inp)):
            if inp[i] == "+":
                sign.append(True)
                num = inp[a:i]
                numbers.append(int(num))
                a = i + 1
            elif inp[i] == "-":
                sign.append(False)
                num = inp[a:i]
                numbers.append(int(num))
                a = i + 1
        # print(sign)
        numbers.append(int(inp[a:]))
        # print(numbers)
        if len(numbers) == n:
            ans = 0
            if sign[0] == False:
                ans += (numbers[0] - numbers[1])
            elif sign[0] == True:
                ans += (numbers[0] + numbers[1])

            for i in range(1,len(numbers)-1):
                if sign[i] == False:
                    ans -= numbers[i + 1]
                elif sign[i] == True:
                    ans += numbers[i + 1]
            print("Teste {}\n{}\n".format(x, ans))
            x += 1