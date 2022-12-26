#WAP a program to print multiplication table of a number

num = int(input("Enter the number : "))

print("The table of "+str(num)+" :")

#1 - using 
i=1
while(i<=10):
    value = num*i
    print(num,"x",i,"=",value)
    i+=1
    
#2 - using for loop
for i in range(1,11):
    value = num*i
    print(num,"x",i,"=",value)
    
    
#F strings
# sentence = f"{num} x {i} = {num*i}"
# print(sentence)