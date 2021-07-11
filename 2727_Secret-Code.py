import string
all_letter = []
for letter in string.ascii_lowercase:
   all_letter.append(letter)

letter_syntex = []
letter_syntex.append('.')
letter_syntex.append('..')
letter_syntex.append('...')
for i in range(0,len(all_letter),3):
    letter_syntex.append(letter_syntex[i]+' .')
    letter_syntex.append(letter_syntex[i+1]+' ..')
    letter_syntex.append(letter_syntex[i+2]+' ...')

while True:
    try:
        n = int(input())
        for i in range(n):
            syntex = input()
            print(all_letter[letter_syntex.index(syntex)])
    except EOFError:
        break