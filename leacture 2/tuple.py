# Tuple: ordered,immutablemallows duplicate elements
mytuple=(["Mango","Apple"],["Red","Green"],"Lion",{"apple":40})

for i in mytuple:
    print(i)

print(type(mytuple[0]))
# As the mytuple zero index is list so we can make a change in that but not in tuple
mytuple[0].append("Orange")
mytuple[0].remove("Mango")

print()
for i in mytuple:
    print(i)

print()
# we can also use the slicing 
print(mytuple[0:3])


