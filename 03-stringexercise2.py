#WAP a program to insert name and date in a letter template

letter = '''
Dear <name>, You are selected on <date>.
Greeting from Tech.pvt.ltfd.
'''

#solution

name = str(input("Enter your name : "))
date = str(input("Enter the date: "))

letter = letter.replace("<name>",name)
letter = letter.replace("<date>",date)

print(letter)