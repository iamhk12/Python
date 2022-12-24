# INPUT

# input are always taken as a string

a = input("Enter Your Name : ")
print(a)
print(type(a)) # string

a = int(a)  # convert a to integer (if possible)

print(type(a)) # int

#OR
# a = int(input("Enter a number")) #taking int input