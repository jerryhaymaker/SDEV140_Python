

import random


def main():
    fileToBeWrittenTo = open('randoms.txt', 'w')
    numberOfRandomNumbers = int(input('Enter the amount of numbers: '))
    for randomNumberCount in range(1, numberOfRandomNumbers +1):
        randomNumber = randomNumberWrite()
        fileToBeWrittenTo.write(str(randomNumber) + '\n')

    print(numberOfRandomNumbers,'numbers inserted into the file.')






def randomNumberWrite():
    randomNumber = random.randint(1, 500)
    return randomNumber

main()

