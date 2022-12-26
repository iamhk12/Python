#WAP  to check whether username is less than 10 characters or not

username = str(input("Enter your username : "))

if(len(username) < 10 ) :
    print("Length is less than 10 characters")
else:
    print("Username approved.")