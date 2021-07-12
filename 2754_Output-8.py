from decimal import Decimal
x = 234.345
y = 45.698
print("{:.6f} - {:.6f}".format(x,y))
print("{:.0f} - {:.0f}".format(x,y))
print("{:.1f} - {:.1f}".format(x,y))
print("{:.2f} - {:.2f}".format(x,y))
print("{:.3f} - {:.3f}".format(x,y))
#Print the two variables with scientific notation with 'e';
print("%.6e - %.6e" % (Decimal(x), Decimal(y)))
#Print the two variables with scientific notation with 'E';
print("%.6E - %.6E" % (Decimal(x), Decimal(y)))
#Print the two variables with use the shortest representation, with 'e' or 'E' or without;
print("%g - %g" %(x,y))
print("%g - %g" %(x,y))