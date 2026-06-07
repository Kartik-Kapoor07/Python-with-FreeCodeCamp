# exception keywords:

# try in this we enter risky code which have the possibility of thwowing an error
# except this block we define type of error and how we should handle that error
# raise it is used to intentionally trigger an exception or error during program execution.
i=True
while i==True:
    try:
        a=(int(input("Enter first number:")))
        b=(int(input("Enter second number:")))
        c=(int(input("Enter third number:")))
        i=False
    except ValueError:
        print("You enter the wrong input,Please try again.")
        
num=sorted([a,b,c])
low,mid,high = num
print(low,mid,high)

# example of rise 
class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError(
            "Value is greater than 100"
        )

    return x

try:

    result = test_value(200)
    print("Value =", result)

except ValueTooHighError as e:
    print("Custom Error:", e)

finally:
    print("Program finished")