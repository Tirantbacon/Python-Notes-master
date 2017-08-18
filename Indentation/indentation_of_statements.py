#  Whitespace determines indentation. Whitespace at the start of logical lines determine the indentation level of the
#  logical line, which in turn is used to determine how statements are grouped.
#  Each statement within a certain indentation level is in a block.
#  For example, the first print function is in the first indentation level
#  The second print function is in the second indentation level.


indentation = 1

if indentation == 1:
    print('I\'m in block', indentation)

indentation = 2

if indentation == 2:
        print('I\'m in block', indentation)


# Ok this is probably not the best example.
#  http://www.python-course.eu/images/blocks.png
