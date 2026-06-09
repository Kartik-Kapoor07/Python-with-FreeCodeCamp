# Logging is used to record what happens in a program while it runs.
# we use it instead of print because sometimes we want to print something for only testing
# we may use it onces in a while so unlike print we dont have to cut each line instead we can use disable function
# and we may not want all the things or error in terminal 

import logging

# Configure logging
logging.basicConfig(
    filename="leacture 2\Logging\App.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

logging.debug(f"User entered values: {num1}, {num2}")

if num2 == 0:
    logging.warning("User entered zero as second number")

try:
    result = num1 / num2
    
    logging.info("Division successful")
    print("Result =", result)

except ZeroDivisionError:
    logging.error("Division by zero attempted")

except Exception as e:
    logging.critical(f"Unexpected error: {e}")

logging.info("Program execution ending")