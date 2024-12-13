

#####################################################
# Positional Notation Key
# !!! = three letter for data type
# &.. = count for data type duplicates
# !!! = month
# &&  = two digit for day of month
# !!! = three letter, firstname, middlename, lastname intial


# Get user input for savings account principal.
flt1oct26jdh = float(input('Enter the amount of principal originally deposited into the account:\n> $'))

# Get user input for annual interest rate.
flt2oct26jdh = float(input('Enter the amount of annual interest rate paid by the account:\n> %'))

# Get user input for compounded interest rate.
int1oct26jdh = int(input('What is the number of times per year the interest is compounded?\n Monthly = 12, Semi-Monthly = 6, Quaterly = 4\n> '))

# Get user input for the number of years the money will grow.
int2oct26jdh = int(input('How many years do you want the account to accumulate interest over time?\n> '))

# Convert percent to decimal.
flt2oct26jdh /= 100

# Calculate compound interest.
flt3oct26jdh = flt1oct26jdh * ((1 + (flt2oct26jdh / int1oct26jdh))**(int1oct26jdh * int2oct26jdh))

# Display the amount of money that will be in the account after the specified number of years to the user.
print(f'Your savings account will have ${flt3oct26jdh:,.2f} after {int2oct26jdh:,d} year(s).')




                           
 
