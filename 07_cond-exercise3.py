#WAP program to check spam message 

txt = str(input("Enter the text/email :"))

isSpam = False

if (txt.find("Buy now") != -1 or txt.find("Make a lot of money") != -1 or txt.find("Click this") != -1):
    isSpam = True

if (isSpam):
    print("SPAM MESSAGE")
else:
    print("NOT A SPAM MESSAGE")
