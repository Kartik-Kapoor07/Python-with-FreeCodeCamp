# Sets: unordered, mutuable, no duplicate exist and doesnot have any index

#unordered and remove duplicate and keep only one
sets={7,5,5,4,37,1,63,6,7,99}
print(sets)

# more knowledge is that a empty set is consider as dict as both have the have same syntax so if we want to create a empty sets you can create like this sets=set()

name=set()

name.add("kartik")
name.add("Rohan")
name.add("Neha")
name.add("Elite")
name.remove("Rohan")
name.discard("katrina")#this is more safer if this name doesent exist then it will not return any error 

print(name)

# clear function in sets

cars=set()

cars.add("Mustang")
cars.add("BMW M5")
cars.add("Mercedes E-Class")
cars.add("Porsche")

print(cars)
cars.clear()
print(cars)

# Conveting string to the sets

word="hello"
print(set(word))

# union combine two or more than two sets

A={1,2,3}
B={3,4,5}

# update()
A.update(B)
print("After update():",A)


# reset A
A={1,2,3}
# intersection_update()
A.intersection_update(B)
print("After intersection_update():",A)


# reset A
A={1,2,3}
# difference_update()
A.difference_update(B)
print("After difference_update():",A)


# reset A
A={1,2,3}
# symmetric_difference_update()
A.symmetric_difference_update(B)
print("After symmetric_difference_update():",A)

# reset A
A={1,2,3}
# It also update set just like update but require new set
x=A.union(B)
print(x)