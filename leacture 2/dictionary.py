# dictionary: unordered, mutable, key value pair, duplicates are not possible and if in any case is two same key have different values then latest value will replace old value

dict1 = {
    "Kartik":0,
    "Kartik":1    
}

print(dict1)

# We can also create dict like this

dict2=dict(Name="Kartik",Age=15,Class=10,Section="Red",Rall_no=20)
print(f"{dict2}\n")
print(dict2["Name"])
print(dict2.get("Name"))# the difference from previous is that is Name doesnot exist the programe will not crash
print(dict2.keys)
print(dict2.values)


# Way to add the data in dict
dict3=dict()

dict3["Email1"] = "xyz@gmail.com"
dict3["Email2"] = "abc@gmail.com"
dict3["Email3"] = "pqr@gmail.com"
dict3["Email4"] = "xyp@gmail.com"
print(dict3)

del dict3["Email3"]

print(dict3)

dict3.pop("Email4")

print(dict3)

# the difference between the del and pop is that we can store the value while poping but cant in del

dict4={"brand": "Ford",
    "model": "Mustang",
    "year": 1964}

for i,j in dict4.items():
    print(f"{i}, {j}")
    
# there are also function like the dict(name), .values, .keys, .items, copy, update can watch on geeks for geeks website no need to code