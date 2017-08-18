

#  Example of using .format to format strings. {} represents the index value of each identifier, or argument.
#  For example, {0} represents the FIRST identifier argument, which in this case is 'name'
#  A comma separates each identifier argument


age = 20
name = 'Dylan'


print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))


#  Numbers can also be omitted, as each pair of curly brackets represents a new index value, starting from 0 and going
# up to 255

#  For example:

behavior = 'cool'
print('{} is my name! Being {} is my game!!'.format(name, behavior))