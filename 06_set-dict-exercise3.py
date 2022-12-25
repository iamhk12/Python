# WAP for four friends to enter their favourite language in a empty dictionary.
# note: Assume names are unique

favLang = {}

# for those with no friends
a = str(input("Enter your favourite language XYZ : "))
b = str(input("Enter your favourite language MNO : "))
c = str(input("Enter your favourite language PQR : "))
d = str(input("Enter your favourite language UVW : "))

favLang = {
    "XYZ": a,
    "MNO": b,
    "PQR": c,
    "UVW": d
}

print(favLang)  # printing in a list form