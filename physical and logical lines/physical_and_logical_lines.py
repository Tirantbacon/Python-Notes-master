#  A physical line is what you see when you write the program in the script editor or interpreter
#  For Example:

#  This is one physical line
my_list = [1, 2, 3, 4]


#  A logical line is what Python sees as a single statement.
#  For Example:

#  This is two physical lines, however python reads it as one single statement (a list),
#  so python sees it as ONE logical line.
my_list = [1, 2,
           3, 4]

# This is an example of one physical line but python reads it as TWO logical lines


print('This is a single physical line\n but the ' r'\n' ' makes python read it as two logical lines')

