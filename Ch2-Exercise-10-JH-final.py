
#####################################################
# Positional Notation Key
# !!! = three letter for data type
# &.. = count for data type duplicates
# !!! = month
# &&  = two digit for day of month
# !!! = three letter, firstname, middlename, lastname intial


# The code below names constants for the cookies recipe.
flt1oct30jdh = 1.5  # num of cups that make up 48 cookies.
int1oct30jdh = 1   # num of cups that make up 48 cookies.
flt2oct30jdh = 2.75 # num of cups that make up 48 cookies.
int2oct30jdh = 48 # num of cookies made from recipe.

# Get user input for specified number of cookies they want to make.
int3oct30jdh = int(input('How many cookies do you want to make?\n> '))

# Calculate how many the users cookies fits into the recipe.
flt3oct30jdh = (flt1oct30jdh / int2oct30jdh) * int3oct30jdh
flt4oct30jdh = (int1oct30jdh / int2oct30jdh) * int3oct30jdh
flt5oct30jdh = (flt2oct30jdh / int2oct30jdh) * int3oct30jdh

# Display to the user how many cups they need for each ingredient for their
# custom recipe.
print(f'For {int3oct30jdh} cookie(s) you need:')
print(f'> {flt3oct30jdh:.2f} cup(s) of sugar.')
print(f'> {flt4oct30jdh:.2f} cup(s) of sugar.')
print(f'> {flt5oct30jdh:.2f} cup(s) of sugar.')
