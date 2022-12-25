#Tuples
#tuple cannot be updated, List can be

t = (1, 2, 3, 4)
print(t[0])  #o/p => 1

#tuple cannot be updated
# t[0] = 34    ERROR : TypeError: 'tuple' object does not support item assignment


t1 = () #empty tuple
print(t1)

#t1 = (1)  #wrong declaration of tuple
t1 = (1,)  #single element #!!! COMMA at end is needed