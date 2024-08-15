"""
student = {
    "name" : "Tohidul Islam",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(len(list(student.keys()))) #Dict.keys
"""

"""
student = {
    "name" : "Tohidul Islam",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
print(list(student.values())) #Dict.values

"""

"""
student = {
    "name" : "Tohidul Islam",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

pairs = list(student.items()) #Dict.items
print(pairs[0])
"""

"""
student = {
    "name" : "Tohidul Islam",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student["name"])  #Dict.get
print(student.get("name")) 
"""

student = {
    "name" : "Tohidul Islam",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
new_dict = {"city" : "Dhaka", "age" : 18 }  #dict_update
student.update(new_dict)
print(student)
