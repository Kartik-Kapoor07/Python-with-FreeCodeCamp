zero = [0,1] * 10
print(zero)

string_list = list("AB") * 10
print(string_list)

def different_arg(a,b, *args , **kwargs):
    print(a,b)
    for arg  in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
        
different_arg(1,2,3,4,Five=5)

def foo(a,b,c):
    print(a,b,c)

my_list = [1,2,3]
my_dict = {'a':1, 'b':2, 'c':3}
foo(*my_list)
foo(**my_dict)

number = [1,2,3,4,5,6,7,8,9]
beginning, *middle, secondlast, last = number
print(beginning)
print(middle)
print(secondlast)
print(last)

# beginning        → 1 fixed (left side)
# secondlast, last → 2 fixed (right side)

# Total fixed = 3

# remaining goes to the middle