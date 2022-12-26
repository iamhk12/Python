#WAP function to print following pattern

'''
n=3

****
***
**
*

'''

def printStar(n):
    for i in range(n):
        print("*"*(n-i)) 
        

printStar(3)