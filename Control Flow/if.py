#  The if statement is used to check a condition.
#  if the condition is true, run a block of statements (called the if-block)
#  (else) process another block of statements (called the else block)
#  The else clause is optional
#  For example:

number = 23
guess = int(input('Enter a number: '))

if guess == number:
    print('Congrats you guessed the number!')
elif guess < number:
    print('Little higher!')
else:
    print('Little lower!')

print('Done')
