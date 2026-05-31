# dacorator
# this is not useful for shorter code but in longer code it is very useful to keep code organised and clean and to keep less number of lines


def greet(word):
    def wrapper():
        print("Before")
        word()
        print("After")
    return wrapper

def hello():
    print("Hello, World!")

greet(hello)()

def logger(func):
    def wrapper():
        print(f"{func.__name__} started")
        func()
        print(f"{func.__name__} finished")
    return wrapper

@logger
def calculate():
    print("Doing calculation")

calculate()