
def main():
    for integerCount in range(1, 101):
        if is_prime(integerCount):
            print(integerCount, end=" ")






def is_prime(specifiedInteger):
    isDivisional = 0
    if specifiedInteger <= 1:
        return False
    for integerCount in range(1, specifiedInteger + 1):
        if specifiedInteger % integerCount == 0:
            isDivisional = isDivisional + 1
            if isDivisional > 2:
                return False
    return True

main()
