def calculate_day(month):
    total = 0
    for i in range(1, month):
        if i == 2:
            total = total + 29
        elif i <= 7:
            if i % 2 == 0:
                total = total + 30
            else:
                total = total + 31
        else:
            if i % 2 == 0:
                total = total + 31
            else:
                total = total + 30
    return total
while True:
    try:
        month, date = input().split()
        month = int(month)
        date = int(date)
        if month == 12 and date == 25:
            print("E natal!")
        elif month == 12 and date == 24:
            print("E vespera de natal!")
        elif month == 12 and date > 25:
            print("Ja passou!")
        else:

            total = calculate_day(month)+date
            xmas = calculate_day(12) + 25
            print("Faltam {} dias para o natal!".format(xmas-total))
    except EOFError:
        break