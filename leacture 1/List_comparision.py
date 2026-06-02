# List comparision it is a concept of creating a new list and comparing it with the old list and it uses few line for example in this code can also also do this thing by making a for loop in that loop taking a variable squaring it then append in new list but it is not recommended because it will take more lines of code and it will be less efficient than using list comprehension. List comprehension is a concise way to create lists and it is more efficient than using for loops. It is also more readable and easier to understand.
number=[1,2,3,4,5,6,7]

other_number=[n**2 for n in number]

print(number)
print(other_number)