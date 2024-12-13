
individualretailpackageprice = 99




# Collect number of user packages purchased
usernumberpackagepuchased = int(input('How many packages have you purchased?\n> '))

if usernumberpackagepuchased < 10:
    retailpackageprice = usernumberpackagepuchased * individualretailpackageprice
    print('You did not qualify for a discount.')
    print(f'Your total price is ${retailpackageprice:,.2f}')

elif 10 >= usernumberpackagepuchased and usernumberpackagepuchased < 20:
    discountedpackageprice = 0.1 # Discounted price for 10-19 packages purchased.
    
elif 20 >= usernumberpackagepuchased and usernumberpackagepuchased < 50:
    discountedpackageprice = 0.2 # Discounted price for 20-49 packages purchased.

elif 50 >= usernumberpackagepuchased and usernumberpackagepuchased < 100:
    discountedpackageprice = 0.3 # Discounted price for 20-49 packages purchased.
    
else:
    usernumberpackagepuchased >= 100
    discountedpackageprice = 0.4 # Discounted price for 100 or more packages purchased.

retailpackageprice = usernumberpackagepuchased * individualretailpackageprice 
totalamountdiscounted = retailpackageprice * discountedpackageprice 
userdiscountedprice =  retailpackageprice - totalamountdiscounted
print(f'Your total price before discount is ${retailpackageprice:,.2f}')
print(f'Your total price after discount is ${userdiscountedprice:,.2f}')
print(f'You saved ${totalamountdiscounted:,.2f}!')











