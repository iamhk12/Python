#WAP to detect double spaces in a string and replace double space with single space

st = "This is a strong with double  spaces."

doublespaces = st.find("  ")
print(doublespaces)

st = st.replace("  "," ")
print(st)