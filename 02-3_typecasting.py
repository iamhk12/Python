# TYPECASTING
# {Changing datatypes}

# Number <-> String

a = "12"
print(type(a))  # string

# print (a+5) #error "int + string"

# trying to change datatype

a = int(a)  # str -> int
print(type(a))  # int

print(a + 5)    # #answer  >> correct

a = str(a)  # int -> str
print(type(a))  # str
