# WAP to give maximum value between two numbers

def maxBetweenTwo(a, b):
    maxi = int
    if (a > b):
        maxi = a
    if (a < b):
        maxi = b
    return maxi

print(maxBetweenTwo(12,9))

# WAP to give maximum value between three numbers

def maxBetweenThree(a,b,c):
    maxi = int
    
    if(a>b and a>c):
        maxi = a
    if(b>a and b>c):
        maxi = b
    if(c>a and c>b):
        maxi = c
        
    return maxi

print(maxBetweenThree(15,98,723))
    
    