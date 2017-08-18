#  The bracket in an escape sequence is always behind whatever should be included
#  For example, if you wanted to show a quotation mark in a string, use a backslash before it.

#  Example of using a single quote escape sequence
print('How much wood can it\'s wood chuck chuck?')
#  Example of using a triple apostrophe escape sequence (not technically an escape sequence but can be helpful)
print('''How much wood can it's wood chuck chuck?''')
#  Example of using a escape sequence within a double quote within a double quote.
print("How much wood can it's \"wood\" chuck chuck?")
#  Example of using a double backslash escape sequence
print("Running \\wood, wood executed!")
