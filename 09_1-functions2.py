# There are two types of functions in python
# 1. Built-in functions.  e.g.: len(), print, etc
# 2. User defined functions.

# Passing multiple arguements

def sumOf(a, b):
    return f"Sum of {a} and {b} is {a+b}"


print(sumOf(15, 16))


# Default arguement parameter

def greet(name="Stranger"):
    print("Good Day,", name)


greet()  # Good Day, Stranger
greet("hk")  # Good Day, hk
