def main():
    try:
        txtFile = open('steps.txt', 'r')
        stepsTaken = 0
        numOfDays = 0
        line = txtFile.readline()

        while line != '':
            numOfDays += 1
            stepsCount =+ int(line)
            stepsTaken += stepsCount
            line = txtFile.readline()

        averageOfstepsCounts = stepsTaken / numOfDays
        avgStepPerMonth = averageOfstepsCounts / 30
    
    except IOError as error:
        print('An IOError occured:', error)
    except ValueError as error:
        print('A ValueError occured:', error)
    else:
        print('Average stepsCount of steps is', avgStepPerMonth)
    finally:
        print(' PROGRAM CLOSED ')
    


main()
