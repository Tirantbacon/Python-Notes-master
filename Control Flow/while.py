#  The while block is like an if block, but loops over and over as long as the
#  given loop continuation condition is true (in this case the given condition is 'running')
#  In this case the while block is known as a loop

number = 23
running = True

while running:
    guess = int(input('Enter an interger: '))

    if guess == number:
        print('Congrats you guessed it!')
        running = False
    elif guess < number:
        print('A little higher!')
    else:
        print('A little lower!')
else:
    print('The loop is over')

print('Done')