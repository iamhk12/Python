# Conditional Statements in python

# PYTHON doesn't have semicolons instead it has indentation

'''
Syntax of if-elif-else
if(condition1):
<indent> statement1
elif(condition2):
<indent> statement2
else:
<indent> statement3

Here, indent means TAB.
'''

# EXAMPLE 1: if-elif-else ladder

a = int(input("Enter your number : "))

if (a > 0):
    print("A is postive")
elif (a < 0):
    print("A is negative")
else:
    print("A is zero")


# EXAMPLE 2 : Multiple if statements
# (no ladder limitation i.e all true statements will be executed)

a = int(input("Enter your new number : "))

if (a < 3):
    print("The value of a is greater than 3")

if (a > 13):
    print("The value of a is greater than 13")

if (a > 7):
    print("The value of a is greater than 7")

if (a > 17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

print("Done")
