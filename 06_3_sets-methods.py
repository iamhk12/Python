# Set Methods/functions

# creating a empty set
b = set()

#########################################################################

# set.add(value)
# Adds a value in a set

b.add(3)
b.add(4)
b.add(5)
# adding a value repetatively does not change a set
b.add(3)
b.add(3)
b.add(3)

# Remider :  Set is a collection of non-repeating elements

print(b)  # {3, 4, 5}

# b.add([4,5,6])  Error : Cannot insert a LIST or DICTIONARY

b.add((4, 5, 6))  # You can insert a tuple

print(b)  # {3, 4, 5, (4, 5, 6)}

#########################################################################


# len(set)
# returns length of set

print(len(b))

#########################################################################

# Set.remove(value)
# To remove a present value from set

b.remove(5)
print(b)

#########################################################################

# Set.pop()
# Removes and return an random element

print(b.pop())

#########################################################################

# Set.clear()
# Makes a set empty

b.clear()
print(b)  # empty set

#########################################################################

a = {1, 3, 4, 5}
b = {5, 6, 7}


# a.union(b)
# #returns --- a union b

print(a.union(b))

#########################################################################

# a.intersection(b)
# #returns --- a intersection b

print(a.intersection(b))
