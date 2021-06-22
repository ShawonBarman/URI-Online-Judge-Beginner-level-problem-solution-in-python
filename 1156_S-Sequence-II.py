s = 1
k = 2
for i in range(3,40,2):
    s = s + (i/k)
    k = 2*k
print("{0:.2f}".format(s))