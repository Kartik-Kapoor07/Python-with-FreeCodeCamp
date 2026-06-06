# Itertools
from itertools import product, permutations, combinations, accumulate, groupby, cycle, repeat, count

a = [1,2,3]
b = [4,5,6]


print("\n========== PRODUCT ==========")

# product() creates the Cartesian product
# It pairs every element of first list with every element of second list
# Example:
# 1 -> (1,4) (1,5) (1,6)
# 2 -> (2,4) (2,5) (2,6)
print(list(product(a,b)))



print("\n========== PERMUTATIONS ==========")

# permutations() changes the order of elements
# Different order = different result

# All possible arrangements of a
print(list(permutations(a)))

# Here 2 means only take 2 elements at a time
# Example: (1,2), (2,1), (1,3), (3,1)
print(list(permutations(a,2)))



print("\n========== COMBINATIONS ==========")

# combinations() creates groups without changing order
# (4,5) and (5,4) are considered the same
# so only one will appear

print(list(combinations(b,2)))



print("\n========== ACCUMULATE ==========")

# accumulate() keeps adding previous values
# Example:
# 1
# 1+2 = 3
# 3+3 = 6

print(list(accumulate(a)))



print("\n========== GROUPBY ==========")

# Function returns True if number < 5
def smaller_than_5(x):
    return x < 5

data1 = [i for i in range(0,10)]

# groupby groups consecutive values having same condition result
group_object = groupby(data1, key=smaller_than_5)

for key, value in group_object:
    print("Key:", key, "Values:", list(value))



print("\n========== CYCLE ==========")

# cycle() repeats items forever
# After reaching end, it starts again from beginning

data2 = ["Apple", "Banana", "Cherry"]

c = cycle(data2)

for i in range(8):
    print(next(c))



print("\n========== REPEAT ==========")

# repeat() repeats same value specified number of times

for value in repeat("Apple",5):
    print(value)



print("\n========== COUNT ==========")

# count(start)
# Starts from given number and keeps increasing forever

cn = count(10)

for i in range(5):
    print(next(cn))
    
# this is the code by chatgpt for better formating and comments but i code fully that in python compiler on website