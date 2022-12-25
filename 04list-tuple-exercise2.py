# WAP a program to accept marks of 6 students and display them in a sorted manner

m1 = int(input("Enter marks for student 1 : "))
m2 = int(input("Enter marks for student 2 : "))
m3 = int(input("Enter marks for student 3 : "))
m4 = int(input("Enter marks for student 4 : "))
m5 = int(input("Enter marks for student 5 : "))

MarksList = [m1, m2, m3, m4, m5]
MarksList.sort()

print(MarksList)