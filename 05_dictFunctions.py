# Dictionary Functions/methods

myDict = {
    "fast": "In a quick manner",
    "hk": "Developer and programmer",
    "marks": [10, 20, 30],
    121203: "Birthdate",
    "newDict": {"Web": "ReactJS"}
}

########################################################################

# Dict.keys()
# Prints all keys.
# type = dict_keys

print(myDict.keys())
# print(list(myDict.keys()))  # makes dict_keys ->list

########################################################################

# Dict.values()
# Prints all values in  a dictionary
# type = dict_values
print(myDict.values())

########################################################################

# Dict.items()
# return key value pairs in a kindoff tuple/list form

print(myDict.items())

########################################################################

print(myDict)

# UpdateDict = {
#     "Bad": "Friend",
#     "HTML": "CSS"
# }

myDict.update({
    "Bad": "Friend",
    "HTML": "CSS",
    "marks" : [100,200,300]
})
print(myDict)

# to add/update contents

########################################################################

# Dict.get(key)
#prints value of a key

print(myDict['hk2']) #error if element is not present
print(myDict.get("hk2"))  #returns none if element is not present

########################################################################
