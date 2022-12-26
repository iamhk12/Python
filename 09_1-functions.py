#Functions

# marks = [45,54,52,12]

# average = sum(marks)/len(marks) 
# print(average)

#Here sum and len are built-in python functions

# Creating a functions

'''
SYNTAX:

def FunctionName (args (optional)):
    statements//
    return value(optional)


'''


marks = [45,54,52,12]

def avg(marks):
    return sum(marks)/len(marks)

print(avg(marks)) # function call

#######################################################################

#WAP to greet a user using function

def greet(name):
    return "Good day, "+name

name = "HK"
print(greet(name))