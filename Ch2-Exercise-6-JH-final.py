
#####################################################
# Positional Notation Key
# !!! = three letter for data type
# &.. = count for data type duplicates
# !!! = month
# &&  = two digit for day of month
# !!! = three letter, firstname, middlename, lastname intial

#define named constants
flt1oct30jdh = 0.05
flt2oct30jdh = 0.025

#input from user for purchase amount
flt3oct30jdh = float(input('Please enter the amount of your purchase: '))

#calculate state tax only
flt4oct30jdh = flt1oct30jdh * flt3oct30jdh

#calculate county tax only
flt5oct30jdh = flt2oct30jdh * flt3oct30jdh

#calculate total sales tax by adding tax values together
flt6oct30jdh = flt5oct30jdh + flt4oct30jdh

#calculate total sale by adding purchase amount by total sale tax
flt7oct30jdh = flt3oct30jdh + flt6oct30jdh

print(f'Your purchase amount is: ${flt3oct30jdh:,.2f}')
print(f'Your state sales tax is: ${flt4oct30jdh:,.2f}')
print(f'Your county sales tax is: ${flt5oct30jdh:,.2f}')
print(f'Your total sales tax is: ${flt6oct30jdh:,.2f}')
print(f'Your total is: ${flt7oct30jdh:,.2f}')
