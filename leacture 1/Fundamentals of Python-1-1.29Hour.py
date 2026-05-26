# variable
# any variable must start with a letter or an underscore(_)
# any variable cannot start with a number or use any space anywhere in its name
# cannot use reserve character like for,if,elif,else etc
# Special characters like @, $, %, or hyphens(-) are not allowed.

# data type
name="kartik"
print(name)
print(type(name))# it will print str as name is a string data type
print(isinstance(name,str))# in we isinstance to get answer in true or false in this we enter a variable who have some data type and then the type of data type we thing that is then it answer in true or false depding weather our assumption is true or not

# conservation
age="15" #this is a string as i had coloum 
print(age)
print(type(age))
Conservation=int(age)
print(type(Conservation))

# or we can also convert it like that age=int("15")

# Arithmetic operators
print(7+1)# it add
print(8-1)#it subtract
print(9*2)#it multiply
print(9**3)# it find power of base and exponent
print(10/4)# it devided even in decimal
print(13//4)# it devide but not in decimal

# we can also combine multiple strings in single line
print("My name is kartik "+"and my age is 15.")
# like this we can also combine multiple variable
x=12
y=3
print(x,y)
# clean way to write variable and message in print by using f string
adress="Guru tej bhadur nagar kapurthala"
print(f"I live in this area {adress}")

# write   each thing in capital or upper letter 
print("paRrOt".upper())
# same with lower letter
print("paRrOt".lower())
# we can also write that for title in this first letter of each word gets into upper letter
print("Peter Piper picked a peck of pickled peppers.A peck of pickled peppers Peter Piper picked.".title())
# we can also check like
print("paRrOt".isupper())#false becausae it doesnot have all its letter in upper case same with title and lower
# way to check the size of the string
print(len(adress))
# way to skip line \n
print('If you are going through hell, keep going"\n — Winston Churchill')

# string characters & slicing
fruit="Apple"
print(fruit[1])# in programming first letter start from zero so when we will write [1] it will give access to the p in word apple and it see from lhs to rhs
print(fruit[-1])# in negtive indexing programe see from rhs to lhs
print(fruit[1:4])# this print letters from 1 to 3 index in python last number is not consisdered

# types of data type
# int it is combination of rational and irrational number
# # bool it have two value true and false and true is consider as 1 and false as 0
# string it store letter,symbol and all

# complex number            
num1=2+3j
num2=complex(2,3)
print(num2.real,num2.imag)

# In operator
name="kartik"
if "k"in name:
    print("k is in name")
# it is used to check whether an item is in a string or not one more example is
print("kar" in name)

# is operator
host1="karti1"
host2="karti2"
host3="karti1"
print(host1 is host2)# it check weather two variable have same memory location or not it doesnot check the value of variable
print(host2 is host1)
print(host3 is host1)