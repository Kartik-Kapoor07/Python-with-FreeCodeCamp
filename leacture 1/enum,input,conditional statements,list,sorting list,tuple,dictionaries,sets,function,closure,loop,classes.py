from enum import Enum

# THIS IS A DATA TYPE USED FOR THE OPTIMIZATION OF CODE FOR SAME TYPE OF VARIABLES AND VALUES
class color(Enum):
    RED=1
    GREEN=2
    BLUE=3
    ORANGE=4

print(len(color))#this will print number of variable we have in enum color datatype
print(type(color))
print(color.RED)
print(color.RED.value)
print(color.RED.name)
print(list(color))

print(color['RED'])   # access by name
print(color(1))       # access by value number

for i in color:
    print(i.name,i.value)#htis will print list of all the enum one by one


# input in python
age=int(input("Enter your age:"))
print(type(age))
print(f"After five year you age will be {age+5}")

# Conditional statements (if, elif, else) allow a program to execute 
# specific blocks of code only if a certain condition is True.

Score=int(input("Enter your score in examination:"))
if Score>=90:
    print("Grade A")
elif Score>=80:
    print("Grade B")
elif Score>=70:
    print("Grade C")
elif Score>=60:
    print("Grade D")
else:
    print("Grade F")
print("Thankyou for giving exam")

# condition under condition
a=(int(input("Enter a number:")))
b=(int(input("Enter a number:")))
c=(int(input("Enter a number:")))

if a==b==c:
    print(f"{a}={b}={c}")

elif a==b:
    if a<c:
        print(f"{a}={b}<{c}")
    else:
        print(f"{c}<{a}={b}")
elif a==c:
    if c<b:
        print(f"{a}={c}<{b}")
    else:
        print(f"{b}<{a}={c}")
elif b==c:
    if b<a:
        print(f"{b}={c}<{a}")
    else:
        print(f"{a}<{b}={c}")
elif a<b<c:
    print(f"{a}<{b}<{c}")
elif a<c<b:
    print(f"{a}<{c}<{b}")
elif b<a<c:
    print(f"{b}<{a}<{c}")
elif b<c<a:
    print(f"{b}<{c}<{a}")
elif c<a<b:
    print(f"{c}<{a}<{b}")
elif c<b<a:
    print(f"{c}<{b}<{a}")
else:
    print("Invalid input")

# list in python 
# a list help to store multiple type of data 
dogs=["roger","susi","lucy","bella"]
print(dogs)#it will print the list
print(dogs.index("susi"))#it will tell the number at which susi is
dogs.append("rocky")#it will add rocky at the end of list
print(dogs)
dogs.remove("susi")#it will remove the susi
print(dogs)
dogs[2]="kartik"#it will replace susi with kartik
print(dogs)
print(dogs[1:3])# it is a method of picking multiple values at  once with the help of slicing
print(len(dogs))
dogs.extend(["minish,14"])#it have the capability to add multiple thing at the end
dogs.insert(2,"banana")
print(dogs)

# sorting lists

number=[1,3,4,5,7,7,3,7,34,2,7,8,2,93]
number.sort()#it make change in real list & it does not return anything
print(number)
number.reverse()
print(number)

grocessary=["Apple","banana","cherry","orange","grapes"]
print(grocessary)
print(sorted(grocessary)) # it will sort list in aphabetical order

# tuple in python
# it is immutable which means it cannot be changed 
tuple_1=(1,2,3,"kartik",True)
print(tuple_1)
tuple_1.count(3)# it will count the number of 3s present in the tuple
tuple_1.index(True)# it will return the index of the true

# Dictionaries
Idendity={"Name":"Kartik kapoor",
          "Age":15,
          "Class":10,
          "Section":"Red",
          "Roll no.":20}

print(Idendity)
print(Idendity["Age"])
print(Idendity.get("Age"))# just a safer side if we enter wrong variable or anything i will print none instead of error
print(Idendity.get("Gender","Male"))# it will first try to find the Gender in dict if it is unable to found that it will print the Male
Idendity["Age"]=20
print(Idendity)

removed_item=Idendity.pop("Section")
print(removed_item)

print(list(Idendity.values()))
print(list(Idendity.keys()))

print(list(Idendity.items()))

# sets

Sets_1 = {"Kartik", "Rahul", "Aman", "Neha", "Rohit"}
Sets_2 = {"Aman", "Neha", "Sahil", "Priya", "Vikram"}

common=Sets_1 & Sets_2
print(common)

combination=Sets_1 | Sets_2# it will print both sets name and it will dont repeat anything
print(combination)

only_in_set1 = Sets_1 - Sets_2
print(only_in_set1)

different = Sets_1 ^ Sets_2
print(different)

# functions
# it is set is instruction that exucute when we call it it may increase number of line but keep code very organised
def greet():
    name=input("Enter your name:")
    print("Hello",name)

greet()

# we can also take the input as parameter in front of out function
def sum(a,b):
    sum=a+b
    print(sum)
sum(2,3)

def product(a=2,b=4):# By assigning default values in the parameters, if we don’t pass any values while calling the function, the default values will automatically be used.
    product=a*b
    print(product)
product()

# Nested function
def talk(phrase):
    def say(word):
        print(word)
    words=phrase.split()
    for i in words:
        say(i)

talk("im going to buy a bunch of grapes")

# closure function function inside function and it can access the variable of outer function
def number_outside():
    number=[]
    def number_inside(y):
        number.append(y)
        print(number)
    return number_inside

add_number=number_outside()
add_number(2)
add_number(3)
add_number(4)

# loop
import random
secrete_number=[]
for i in range(101):
    secrete_number.append(i)

computer_choice=random.choice(secrete_number)

i=True
attempt=0

while i==True:
    User_guess=int(input("Enter the number between 1 and 100:"))
    attempt+=1

    if User_guess==computer_choice:
        print("Congratulations!")
        i=False

    elif User_guess>computer_choice:
        print("The number is lower")

    else :
        print("The number is higher")
        attempt+=1

print("Total attempt taken to guess the number is  ",attempt)

# break and continue statement
for i in range(1,6):
    
    if i==3:
        break
    print(i)
print()
for i in range(7,12):
    
    if i==9:
        continue
    print(i)

# classes
class person():
    name="kartik"
    occupation="student"
    networth=45
    def info(self):
        print(f"{self.name} is a {self.occupation} and his networth is {self.networth} ")
person1=person()
person1.info()# Update learning
