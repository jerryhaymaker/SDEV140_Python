def main():
    try:
        txtFile = open('numbers.txt', 'r')
        total = 0
        linesOfCode = 0
        line = txtFile.readline()

        while line != '':
            linesOfCode += 1
            total =+ int(line)
            line = txtFile.readline()

        averageOfNumbers = total / linesOfCode
    
    except IOError as error:
        print('An IOError occured:', error)
    except ValueError as error:
        print('A ValueError occured:', error)
    else:
        print('Average of number is', averageOfNumbers)
    finally:
        print(' PROGRAM CLOSED ')


main()
