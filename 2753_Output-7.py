import string
all_letter = []
for letter in string.ascii_lowercase:
   all_letter.append(letter)

a = 0
for i in range(97,123):
    print("{} e {}".format(i, all_letter[a]))
    a += 1