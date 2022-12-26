#WAP to check whether a given number is prime or not

num = int(input("Enter your number : "))

isPrime = True

for i in range(2,num):
    if(num%i==0):
        isPrime = False
        break

if(isPrime):
    print("Your input is a prime number.")
else:
    print("Your input is not a prime number.")
    