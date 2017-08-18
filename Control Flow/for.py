#  This is a for block
#  the for statement goes over each item in a sequence (whether it be a number or a string)
#  in this case each number in the range 1 to 5 is passed as a random identifier variable called 'i'
#  the for loop goes through EACH value, and each number is printed with the print function.
#  Once the entire range has been iterated (gone through), the else block is executed.
#  In this case, the for loop does not repeat over and over, but only once.

for i in range(1, 5):
    print(i)
else:
    print('The loop is over!')