

notationnnumber = int(input('Enter a nonnegative number: '))

while notationnnumber <0:
    print('n\This is not a nonnegative number.')
    notationnnumber = int(input('Enter a nonnegative number: '))

if notationnnumber == 0:
    print('n\0! = 1')
else:
    nonnegativefactorialnumber = 1
    for factorialintegernumber in range(notationnnumber, 0, -1):
        nonnegativefactorialnumber *= factorialintegernumber
    print('\n ' + str(notationnnumber) + '! = ' + str(nonnegativefactorialnumber))
