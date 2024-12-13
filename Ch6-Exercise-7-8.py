
def main():
    displayNumbers('randoms.txt')


def displayNumbers(fileToBeRead):
    randomNumbersFile = open(fileToBeRead, 'r' )

    total = 0
    numberOfRandomNumber = 0
    line = randomNumbersFile.readline()

    while line != '':
        numberOfRandomNumber += 1
        randomNumber = int(line)
        total += randomNumber
        print(randomNumber)
        line = randoms.txt.readline()

        print('n\The total of all the numbers in the file is ' + str(total) +\
              '\nThere are ' + str(numberOfRandomNumbers)+ \
              ' numbers in the file ')










main()
