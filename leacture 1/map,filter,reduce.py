# map apply one function to all items in an list,tuple etc and return a new list

number=[1,2,3,4,5]

result=map(lambda x:x*2,number)
print(tuple(result))

# filter

def isEven(n):
    return n % 2 == 0
    
for i in range (0,3):
    result=isEven(number[i])
    print(result)

even_nums = list(filter(isEven, number))
print(even_nums)

# reduce
from functools import reduce

expense=[
    ('dinner',350),
    ('movie',500),
    ('snacks',150)
]

sum=reduce(lambda x,y: x + y[1], expense,0)
print(sum)# Update learning
