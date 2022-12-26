# how to prevent new line in print python function
# ANS ::  print("____",end="")


#WAP to calculate sum of first n natural numbers using recursion
#Take n as input 

def sumTillN(n):
    if(n == 0):
        return 0
    
    return n + sumTillN(n-1)

num = int(input("Enter n : "))
print(f"The sum till {num} is {sumTillN(num)}")

