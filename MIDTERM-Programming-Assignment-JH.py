
wordList = []
wordsFromUser = input('Enter first word of your sentence: ').strip()

while wordsFromUser != 'end_here':
    wordList.append(wordsFromUser)
    wordsFromUser = input('Please enter the next word of your message or ' \
                          'type "end_here" when done: ')

    fullSentence = ' '.join(wordList).capitalize()

print("\n", end='')
print(fullSentence)

counter = 0
for word in wordList:
    counter = counter + 1
print("\n", end='')
print ("There are " + str(counter) + " words in the sentence.")

