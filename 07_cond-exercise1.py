# WAP to find the greatest of four numbers entered by the user

a = int(input("Enter no. 1 : "))
b = int(input("Enter no. 2 : "))
c = int(input("Enter no. 3 : "))
d = int(input("Enter no. 4 : "))


# Approach 1
if (a > b and a > c and a > d):
    print(a, "is the greatest integer.")
elif (b > a and b > c and b > d):
    print(b, "is the greatest integer.")
elif (c > b and c > a and c > d):
    print(c, "is the greatest integer.")
elif (d > b and d > c and d > a):
    print(d, "is the greatest integer.")

# Approach 2
if (a > b):
    x = a
else:
    x = b

if (c > d):
    y = c
else:
    y = d

if (x > y):
    print(x, "is the greatest integer.")
else:
    print(y, "is the greatest integer.")
