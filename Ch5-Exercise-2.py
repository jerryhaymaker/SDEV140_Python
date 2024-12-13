

#define named constants
stateSalesTax = 0.05
countySalesTax = 0.025

def main():
    amtOfUserPurchase = float(input('Please enter the amount of your purchase: '))
    totalStateSalesTax = stateSalesTax * amtOfUserPurchase
    totalCountySalesTax = countySalesTax * amtOfUserPurchase
    totalSalesTax = totalStateSalesTax + totalCountySalesTax
    totalPurchaseAmt = amtOfUserPurchase + totalSalesTax

    print(f'Your purchase amount is: ${amtOfUserPurchase:,.2f}')
    print(f'Your state sales tax is: ${totalStateSalesTax:,.2f}')
    print(f'Your county sales tax is: ${totalCountySalesTax:,.2f}')
    print(f'Your total sales tax is: ${totalSalesTax:,.2f}')
    print(f'Your total is: ${totalPurchaseAmt:,.2f}')




main() 
    
