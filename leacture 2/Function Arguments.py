# topics to studey

# *- The difference between arguments and parameters
# *- Positional and keyword arguments
# *- Default arguments
# *- Variable-length arguments (*args and ** kwargs)
# *- Container unpacking into function arguments
# *- Parameter passing (by value or by reference?)

print("--arguments and parameters--")
def print_name(name): # it takes arguments
    return name
    
print(print_name("Kartik")) # it is parameter

print("--Positional and keyword--")
def student(name, age, grade):
    return f"Name: {name}, Age: {age}, Grade: {grade}"

# Positional → order matters
student("Alice", 20, "A")

# Keyword → order doesn't matter
student(age=20, grade="A", name="Alice")

print("--Default arguments--")
def power(base,exponent=2):# default argument act when there is no value for a value
    return base**exponent

print(power(3))       # uses default exp=2 → 9
print(power(3, 3))    # overrides default → 27

print("--*args and ** kwargs--")
def add(*args):
    print(type(args))   # <class 'tuple'>
    return sum(args)

print(add(1, 2, 3, 4))     # 10

# **kwargs → multiple keyword arguments (dict)
def display(**kwargs):
    print(type(kwargs))     # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display(name="Alice", age=20, city="NYC")

print("--CONTAINER UNPACKING INTO ARGUMENTS--")
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))           # unpacking list → positional

info = {"a": 1, "b": 2, "c": 3}
print(add(**info))          # unpacking dict → keyword

# Immutable types (int, str, tuple) → like PASS BY VALUE
def change_int(n):
    n = 100     # only changes local copy
    print("Inside:", n)

num = 5
change_int(num)
print("Outside:", num)  # still 5 ← unchanged

# Mutable types (list, dict, set) → like PASS BY REFERENCE
def change_list(lst):
    lst.append(99)      # modifies the original!
    print("Inside:", lst)

my_list = [1, 2, 3]
change_list(my_list)
print("Outside:", my_list)  # [1, 2, 3, 99] ← changed!