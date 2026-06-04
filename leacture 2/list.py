# List : orderred,mutable,allow duplicate element 

# orderred it will keep the same order
mylist1 = ["apple", "banana", "mango"]
print(mylist1)

# mutuable can make changes
mylist2 = ["apple", "banana", "mango"]

mylist2[1] = "orange"   # change item
mylist2.pop(0)
mylist2.append("Cherry")
mylist2.insert(0,"Dragon")
print(mylist2)

# Allow duplicates
mylist3 = ["apple", "banana", "apple", "mango"]
print(mylist3)

# Sorted list in number
mylist4=[-5,5,-9,-2,6,-22]
x=sorted(mylist4)# This sorts the list in ascending order 
print(x)

# sorted list in bool
mylist5=[True,False,True,False,False]
y=sorted(mylist5)#this sorts from false to true because false=0 and true=1
print(y)

# sorted in string
mylist6=["Wallace","Dayton","ryker","mazie"]
z=sorted(mylist6)# in python string is sorted based in upper-case and lower-case and second criteria is first alphabet starting alphabets get priority and if first alphabet is same then it will see the second and it keep going like this
print(z)

# sorting it is just like sorted but in this we directly make a change in mylist and dont need to make a another variable

mylist7=[-1,-2,-3,-4,1,2,3,4,5]
mylist7.sort(reverse=True)
print(mylist7)