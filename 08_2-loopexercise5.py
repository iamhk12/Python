# WAP to print the following patterns :

'''
Q1:

n=4

*
**
***
****

'''

n = 4

for i in range(4):
    print("*" * (i+1))


'''
Q2:

n=3

  *
 ***
*****

'''


n = 3

for i in range(3):
    print(" "*(n-i-1), end="")
    print("*"*(2*i+1), end="")
    print(" "*(n-i-1))
