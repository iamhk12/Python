# WAP a program to input eight numbers and display all the unique no.s once.

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
num4 = int(input("Enter number 4 : "))
num5 = int(input("Enter number 5 : "))
num6 = int(input("Enter number 6 : "))
num7 = int(input("Enter number 7 : "))
num8 = int(input("Enter number 8 : "))

mySet = {num1, num2, num3, num4, num5, num6, num7, num8, }

print(mySet)

####################################################################

# is this possible
# ->
#  SetofX = {18, "18"}

# "Answer is YES", both of them are unique according to python,
# since datatypes are different.


####################################################################
# QUES: What is the length of s ?
# s = {20, 20.0, "20"}

#Answer => length of s is 2

####################################################################

#Ques :  What is the type of s ?
# s = {}

#Answer => s is a empty DICTIONARY.
