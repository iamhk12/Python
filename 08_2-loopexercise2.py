# WAP to greet all names in a list which start with H

listOfNames = ["Hk", "Hlop", "Xyz", "Mno"]

for name in listOfNames:
    if (name.startswith("H")):  # 1
        # if(name.find("H")==0): #2
        print(f"Hello, {name}") #f-string
