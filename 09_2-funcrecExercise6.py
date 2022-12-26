#WAP a program to print multiplication table of a number using functions

def multTable(num):
    print(f"The Multiplication table of {num} :")    
    for i in range(1,11):
        value = num*i
        print(num,"x",i,"=",value)
        
multTable(5)