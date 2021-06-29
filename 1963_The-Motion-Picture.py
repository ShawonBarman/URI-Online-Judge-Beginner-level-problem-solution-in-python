old_price, new_price = input().split()
old_price = float(old_price)
new_price = float(new_price)
percen_price = ((new_price-old_price)/old_price)*100
print("{:.2f}%".format(percen_price))