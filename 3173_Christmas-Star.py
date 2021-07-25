n = int(input())
jupiter_total_day = (2020*365 + 12*30 + 21) + int(4346.5 * n)
saturno_total_day = (2020*365 + 12*30 + 21) + int(10811.5 * n)
j_years = jupiter_total_day // 365
s_years = saturno_total_day // 365
j_months = (jupiter_total_day - j_years *365) // 30
s_months = (saturno_total_day - s_years *365) // 30
j_days = (jupiter_total_day - j_years * 365 - j_months*30)
s_days = (saturno_total_day - s_years * 365 - s_months*30)
print("Dias terrestres para Jupiter = {}".format(int(4346.5 * n)))
print("Data terrestre para Jupiter: {}-{}-{}".format(j_years, j_months, j_days))
print("Dias terrestres para Saturno = {}".format(int(10811.5 * n)))
print("Data terrestre para Saturno: {}-{}-{}".format(s_years, s_months, s_days))

#this solution has Wrong answer (5%)