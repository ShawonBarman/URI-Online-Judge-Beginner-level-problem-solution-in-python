n = ""
arr = []
while n != "</html>":
    n = input()
    arr.append(n)
i = arr.index("    <body>")
i += 1
while arr[i] != "    </body>":
    print(arr[i])
    i += 1
