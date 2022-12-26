#WAP a program to print multiplication table of a number in a reversed order

num = int(input("Enter the number : "))

print("The table of "+str(num)+" :")

#1 - using 
i=10
while(i>0):
    value = num*i
    print(num,"x",i,"=",value)
    i-=1
    