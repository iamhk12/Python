#Recursion is calling of a function in the same function

#Write a program for factorial of a number

def fact(n):
    if(n==0):
        return 1
    
    return n*fact(n-1)

print (fact(3))


#