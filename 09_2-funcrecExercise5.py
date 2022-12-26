
#Strip in a string

'''
before String.strip()//
string = "     Hello This is HK     "
string.strip()

AFTER: 
string = "Hello This is HK

'''

#WAP function to remove a given word from a string 
#... and strip it at the same time


def removeAndStrip(String, word):
    newStr = String.replace(word, "")
    newStr = newStr.strip()
    
    return newStr

letter = "       Hello, This is HK Programmer.               "

newLetter = removeAndStrip(letter,"Programmer")

print(newLetter)