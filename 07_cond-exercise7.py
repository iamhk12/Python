#WAP to check whether a post is talking about hk or not

post = str(input("Enter your post : "))

#Making the whole string in lower case so detection becomes easy
post = post.lower()

if(post.find("hk")!=-1):
    print("The post is relevant to hk.")
else:
    print("The post is not relevant to hk.")    
    