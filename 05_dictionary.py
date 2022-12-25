# Dictionary

# Set of keys and values

myDict = {
    "Fast": "In a quick manner",
    "HK": "Developer and programmer",
    "Marks": [10, 20, 30],
    121203: "Birthdate",
    "newDict": {"Web": "ReactJS"}
}

print(myDict["Fast"])  # O/P =>In a quick manner
print(myDict["Marks"])  # O/P =>[10, 20, 30]
print(myDict["newDict"])  # O/P =>{'Web': 'ReactJS'}
print(myDict["newDict"]["Web"])  # O/P =>ReactJS


# Dictionary is change-able , i.e :

myDict["HK"] = "Data Scientist"
print(myDict["HK"])  # O/P => Data Scientist
