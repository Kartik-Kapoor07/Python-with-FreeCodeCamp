# Lambda
from functools import reduce

# the sorted list fucntion sort the list based on the x value and using the lambda functoin we make y treat as x
print("---Sort the list by ascending order of y")
list_number=[(1,5),(2,4),(3,3),(4,2),(5,1)]

a=sorted(list_number,key=lambda x:x[1])
print(list(a))

# map and lambda and map are mainly used to memory efficiet as it give the hex value of ram not the result until we force
print("---Map with lambda---")
a = [1,2,3,4,5,6,7,8]
b = map(lambda x:x*2,a)
print(b)
print(list(b)) 

# reduce it sores the lambda function value and then lambda use to update that value and works until work is complete
print("---reduce---")
grocery = [
    ("Ball",400),
    ("Protein drink",300),
    ("Bottle", 750)
]

reduce_func= reduce(lambda x,y: x+y[1],grocery,0)
print(reduce_func)

# fully coded by myself taken inspiration from gpt from yesteday code that to make output good in look how should i have to code