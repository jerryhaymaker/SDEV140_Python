



# Accumulator
totalusersalary = 0 


# Get user input for how many day they have worked
userdaysworked = int(input('How many days did you work? '))

for numberofdays in range(1, userdaysworked + 1):
    userdailypay = 0.01 * 2 ** (numberofdays -1) # Doubles each day.
    totalusersalary += userdailypay # Increment totalusersalary with userdailypay.    
print(format(numberofdays, ), '$' + format(userdailypay,))
        
