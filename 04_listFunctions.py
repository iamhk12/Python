# List Methods/Functions
# https://docs.python.org/

a = [1, 4, 76, 43, 2, 21]

###############################################################

# List.sort()
# Sorts the original list in itself

print(a)  # [1,4,76,43,2,21]

a.sort()
print(a)  # [1, 2, 4, 21, 43, 76]

###############################################################

# List.reverse()
# reverses the original list

a.reverse()
print(a)

###############################################################

# List.append(value)
# Add an value at the end of the original list

a.append(96)
print(a)

a.append(1947)
print(a)

###############################################################

# List.insert(index, value)
# inserts a value at an index

print(a)  # [76, 43, 21, 4, 2, 1, 96, 1947]

a.insert(3, 1950)
print(a)  # [76, 43, 21, 1950, 4, 2, 1, 96, 1947]

###############################################################
# List.pop() and List.remove()

a.pop(4) #pops an element at the given index
a.remove(1947) #pops an element given

print(a)

###############################################################