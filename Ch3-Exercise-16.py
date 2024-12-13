

# Collect year from user.
collectyearfromuser = int(input('Enter a year: '))

# Named constant
calculateddayofmonth = ''

# Calculate if the user year is leap year.
if collectyearfromuser % 100 == 0:
    if collectyearfromuser % 400 == 0:
        calculateddayofmonth += '29'
    else:
        calculateddayofmonth += '28'
else:
    if collectyearfromuser % 4 == 0:
        calculateddayofmonth += '29'
    else:
        calculateddayofmonth += '28'
print(f'February in the year {collectyearfromuser} has {calculateddayofmonth} days.')
        
