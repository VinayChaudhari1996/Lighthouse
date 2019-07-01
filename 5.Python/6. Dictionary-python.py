"__Author__"=="Amar Singh"

d = {}    # empty dictionary
d = {"name":"Amar_singh",
    "Age":24,
    "Designation":"Python developer"}

print(d)        # Return all data

print(d["name"])        # return all values of names
print(d.keys())         # return all keys from dictionary
print(d.values())       # return all values from dictionary

print(d.fromkeys(d))     # return all copied keys from dictionary

# Note  fromkeys use for creating new dictionary from existing dictionary with all key 

# create list of value inside dictionary

d1 = {
        "Name":["chinny","bunny","sunny"],
        "Age":[23,24,25],
        "Address":["chunagarh","devil","heaven"]

}

print(d1)

print(d1["Name"])  # return all data of names
print(d1["Name"][1])  # return names first index value

print(d1.items())  # return all value (key,value) pairs

d1.pop("Name")   # remove name key with value in the dictionary


# Note :- you can also practice all builtin function in dictionary