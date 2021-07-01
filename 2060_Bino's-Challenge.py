num = int(input())
numbers = list(map(int, input().split()))[:num]
count_two = 0
count_three = 0
count_four = 0
count_five = 0
for i in range(len(numbers)):
    if numbers[i]%2 == 0:
        count_two += 1
    if numbers[i]%3 == 0:
        count_three += 1
    if numbers[i]%4 == 0:
        count_four += 1
    if numbers[i]%5 == 0:
        count_five += 1
print("{} Multiplo(s) de 2".format(count_two))
print("{} Multiplo(s) de 3".format(count_three))
print("{} Multiplo(s) de 4".format(count_four))
print("{} Multiplo(s) de 5".format(count_five))