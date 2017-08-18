theNumber = 413

guess = int(input('Enter a number!: '))

if guess == theNumber:
    print('Congrats you guessed the number!')
elif guess < theNumber:
    print('A little lower!')
else:
    print('A little higher!')

