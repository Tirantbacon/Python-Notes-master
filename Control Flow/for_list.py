#  A for block can also iterate through a list of strings

food = ['Hamburgers', 'Apple pies', 'Cheeseburgers', 'Bananas']
for f in food:
    print(f, len(f))

#  Notice how the range function is not used. Considering the list defines literal strings, and not integers,
#  it is not a range
