#  Compound statements contain groups of other statements (two or more)
#  They affect or control the execution of those statements in some way

#  A compound statement consists of one or more clauses
#  Clauses consist of a header and a suite
#  A header typically is the first line of a compound statement, and contains a :, and controls the suite that follows

#  A suite is the group of statements inside the compound statement.
#  A separating header is the second header that controls the next set of statements, typically if the first
#  set of statements does not execute.
#  For example:

variable = int(input('Enter number!'))

if variable >= 100:  #  header
    print('The variable is true!')  #  Statement
else:   #Seperating header
    print('The variable is not true!')  #  Statement
