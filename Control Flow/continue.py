#  The continue statement skips the rest of the statements in the block.
#  In this case if the length is < 3, too small is printed, and instead of the print function being
#  executed, it is skipped, and the loop returns to it's initial state (waiting for input)
#  If the continue statement was not executed, the print function at the end of the compound statement
#  would be executed each time something was inputted.

while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is sufficient length')
