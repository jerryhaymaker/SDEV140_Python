

print('Hello! Welcome to the Wi-Fi connection troubleshooter.')
print('Please answer "yes" or "no" to the following questions truthfully.\n')

# Named constant
truefalsedecision = ''


print('Please reboot the computer and try to connect.')
truefalsedecision = input('did that fix your problem? ')
if truefalsedecision == 'no':
    print('\nPlease reboot the router and try to connect.')
    truefalsedecision = input('Did that fix your problem? ')
    if truefalsedecision == 'yes':
        print('\nGreat! Im happy that fixed your issue!')
    if truefalsedecision == 'no':
        print('\nPlease make sure the cables between the router are plugged in firmly.')
        truefalsedecision = input('Did that fix your problem? ')
        if truefalsedecision == 'no':
            print('\nPlease move the router to a new location.')
            truefalsedecision = input('Did that fix your problem? ')
            if truefalsedecision == 'no':
                print('\nGet a new router.')
    
    
    
