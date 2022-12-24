# Strings in python
name = "Himanshu"
greeting = "Good Morning, "
# print(type(name))


# Concatenating
print(greeting + name)

c = greeting + name
print(c)

# String character index start  from 0 to (length - 1)

print(name[0])  # O/P => H
print(name[3])  # O/P => a

# IMPORTANT!
# name[3] = k  ===== this is not supported (error)

# Slicing
print(name[0:3])  # printing 0,1,2 => Him #from 0 till before 3

print(name[0:])  # print(name[0:(maximum no. => len)])
print(name[:4])  # print(name[(minimum no. => 0):4])

# Negative indices

hello = "hello"
x = hello[-4:-1]  # same as hello[1:4]
print(x)


d = hello[1:4:1]  # nothing is skipped coz skip value is 1
print(d)

word = "Hello, This is Himanshu Kothari"

e = word[1::2]  # every second element starting from index1 to end is skipped
print(e)
