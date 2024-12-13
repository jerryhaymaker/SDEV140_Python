
def main():
    displayNumbers('randoms.txt')


def displayNumbers(fileToBeRead):
    randomNumbersFile = open(fileToBeRead, 'r' )

    total = 0
    numberOfRandomNumbers = 0
    line = randomNumbersFile.readline()

    while line != '':
        numberOfRandomNumbers += 1
        randomNumber = int(line)
        total += randomNumber
        print(randomNumber)
        line = randomNumbersFile.readline()

        print('\nThe total of all the numbers in the file is ' + str(total) +\
              '\nThere are ' + str(numberOfRandomNumbers)+ \
              ' numbers in the file ')










main()
