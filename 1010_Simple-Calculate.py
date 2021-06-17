product_1, number_units_1, units_price_1 = input().split()
product_2, number_units_2, units_price_2 = input().split()

ans = (int(number_units_1)*float(units_price_1))+(int(number_units_2)*float(units_price_2))
print("VALOR A PAGAR: R$ {0:.2f}".format(ans))