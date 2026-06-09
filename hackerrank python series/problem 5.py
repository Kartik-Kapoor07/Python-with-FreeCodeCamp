# Task
# The provided code stub reads an integer, n , from STDIN. For all non-negative integers i<n, print i².

# Sample Input 0

# 5
# Sample Output 0

# 0
# 1
# 4
# 9
# 16

n=int(input(""))

for i in range(0,n):
    square=i**2
    print(square)