def main():
    UPPER_COUNT = 0
    LOWER_COUNT = 0
    DIGIT_COUNT = 0
    DIGIT_COUNT = 0
    UPPER =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    LOWER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    DIGIT = ['0','1','2','3','4','5','6','7','8','9']
    whitespace = [' ']
    FILE_IN_DATA = open("text.txt", "r")
    DATA = FILE_IN_DATA.read()
    for CHARACTER_COUNT in DATA:
        if CHARACTER_COUNT in UPPER:
            UPPER_COUNT += 1  
        elif CHARACTER_COUNT in LOWER:
            LOWER_COUNT += 1
        elif CHARACTER_COUNT in DIGIT:
            DIGIT_COUNT += 1
        elif CHARACTER_COUNT in whitespace:
            DIGIT_COUNT += 1
            
    print('The uppercase count is',UPPER_COUNT)
    print('The lowercase count is',LOWER_COUNT)
    print('The digit count is',DIGIT_COUNT)
    print('The whitespace count is',DIGIT_COUNT)

main()
