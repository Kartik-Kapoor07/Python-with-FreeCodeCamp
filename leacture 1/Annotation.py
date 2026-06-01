# Annotations are type hints that describe the expected types of variables,
# function parameters, and return values.
# They are optional and are not enforced by Python at runtime.
# Annotations help developers, IDEs, and type-checking tools understand code better.

def add(a:int,b:int)->int:
    return a+b

print(add(5,10)) # it will return 15
print(type(add(5,10))) # it will return <class 'int'>
print(add("Hello ","World")) # it will return "Hello World" but it is not recommended to use it because it can lead to errors in the future when we try to add two different types of data.
print(type(add("Hello ", "World"))) # it will return <class 'str'>

print(add.__annotations__) # it will return {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>} which is the annotation of the function add.# Update learning
