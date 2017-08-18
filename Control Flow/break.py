#  The break statement is used to break out a loop statement
#  This means it's used to stop the execution of a looping statement
#  even if the loop continuation condition has not become false

while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    else:
        print('The length of the string is', len(s))
print('Done!')
