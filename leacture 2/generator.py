# A generator is a special type of function that produces a sequence of values lazily 
# — one at a time, only when asked — instead of computing and storing everything in memory at once.
# this is used for memory efficiency 
# it just rember where it stop so that if need to run again generator know from where to run

# yield run only once a time when called because they dont rember things
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3



def countdown(n):
    while n > 0:
        yield n      # pauses here, sends n to caller
        n -= 1       # resumes here on next next()

for val in countdown(5):
    print(val)       # 5, 4, 3, 2, 1
    
# List comprehension — builds entire list in memory
squares_list = [x**2 for x in range(1000000)]

# Generator expression — computes one at a time
squares_gen = (x**2 for x in range(1000000))

print(squares_list)
print(next(squares_gen))   # 0
print(next(squares_gen))   # 1

def fibonacci(limit):
    a, b = 0, 1
    while a<limit:          # infinite loop — safe because of yield
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(8):
    print(next(fib))     # 0 1 1 2 3 5 8 13