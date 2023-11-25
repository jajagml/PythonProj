# dictionary - used to store data values in key:value pair
# collection that is ordered, changeable, and do not allow duplicates
# Dictionaries cannot have two items with the same key
empProfile = {
    "First name" : "John",
    "Middle name" : "M.",
    "Last name" : "Smith",
    "DOB" : "10/30/2001",
    "Salary" : 1000,
}

# Access value
print(empProfile["DOB"]) # way 1)
print(empProfile.get("Salary")) # way 2

# get the keys and put it in a list
iKeys = empProfile.keys()
print(iKeys)

# get the values and put it in a list
iKeys = empProfile.values()
print(iKeys)
# update the value of the key
empProfile["Salary"] = 2000
print(empProfile["Salary"])

# returns the items together with its keys
iItems = empProfile.items()
print(iItems)

if "Salary" in empProfile: # only keys can use in this condition; put .values to use in condition
    print("Yes")

# Update dictionary
empProfile.update(
    {"Salary":"3000",
     "First name": "James"})
print(empProfile["Salary"])
print(empProfile["First name"])

# Add keys to dictionary using update
empProfile.update({"Position":"Senior"})
print(empProfile["Position"])

# Add keys and values
empProfile["addedKey"] = "addedItem"
print(empProfile["addedKey"])

# Remove items from dictionary
# pop - will remove the item based on the specified key
empProfile.pop("addedKey")
print(empProfile)

# popitem - will remove the last inserted item 
empProfile.popitem()
print(empProfile)

# del dictionary - removes the item based on the specified key
del empProfile["DOB"]
print(empProfile)

# del - will delete the specified dictionary
# .clear() - will clear the specified dictionary

# loop dictionary can be by keys, values
for info in empProfile:
    x = "{}: " + empProfile[info]
    print(x.format(info))

# loop for items in dictionary
for iKeys, iItems in empProfile.items():
    x = "{0}: " + "{1}"
    print(x.format(iKeys, iItems))

# copy dictionary
copyEmpProfile1 = empProfile.copy()
print(copyEmpProfile1)
# copy dictionary using dict()
copyEmpProfile2 = dict(empProfile)
print(copyEmpProfile2)

# nested dictionary
# dictionaries within dictionary
empProfile = {
    "emp1":{
    "First name" : "Jane",
    "Middle name" : "A.",
    "Last name" : "Swift",
    "DOB" : "10/30/1989",
    "Salary" : 3000,
    },
    "emp2":{
    "First name" : "Joseph",
    "Middle name" : "D.",
    "Last name" : "Mari",
    "DOB" : "12/25/1989",
    "Salary" : 4000,
    }
}
print(empProfile["emp1"]["First name"])
print(empProfile["emp2"]["First name"])

# how to update items from nested dictionary
empProfile.update({"emp2":{
    "First name" : "Disney",
    "Middle name" : "D.",
    "Last name" : "Walter",
    "DOB" : "12/25/1890",
    "Salary" : 2000,
}})
print(empProfile["emp2"]["First name"])

emp4 = {
    "First name" : "Bruno",
    "Middle name" : "P.",
    "Last name" : "Mars",
    "DOB" : "03/25/1989",
    "Salary" : 1500,    
}
print(empProfile)
print("---------")
empProfile.update({"emp4" : emp4}) 
print(empProfile)

# assigning to the nested dictionary
# empProfile = {"emp4" : emp4} 
# print(empProfile)
