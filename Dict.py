# dictionary is used to store data values in key -value pairs
# ordered mutable  no duplicate keys

info = {
    "key" : "value",
    "name" : "kgs",
    "learn" : "python",
    "marks" : 50,
    "is passed" : True,
    "list" : [1,2,3],
    "tup" : (4,5,6),
    "list1" : [1,"hello",3],
    12 : 34.4,
    2.3 : 233.3333
}
print(info)
print(type(info))
print(info["list"])

info["name"] = "arjun"
print(info)
info["surname"] = "kapoor"
print(info)
info["surname"] = 22
print(info)

# nesting in python

student = {
    "name" : "atul",
    "score" : {
        "chem" : 98,
        "phy"  : 97,
        "math" : 90
    }
}

print(student)
print(student.keys())
print(student.values())
print(student.items())
print(student["score"])
print(student["score"]["phy"])

pairs = list(student.items())
print(pairs[0])
print(student.get("score"))
print(student.get("kgs"))

#update method

student.update({"city" : "delhi"})
print(student)


marks = {}

x = int(input("enter phy marks : "))
marks.update({"phy":x})

x = int(input("enter chem marks : "))
marks.update({"chem":x})

x = int(input("enter math marks : "))
marks.update({"math":x})

print(marks)