#WAP whether a given name is present in a list or not

listOfNames = ["hk","xyz","mon","abc","pqr"]

name = str(input("Enter your name to check : "))

if(name in listOfNames):
    print("Your name is present in list.")
else:
    print("Your name is not present in list.")