# Exception handling in a python

def calculator():
    History = []

    while True:
        try:
            print("\nSelect the operator:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Modulus (%)")
            print("6. Exponentiation (^)")
            print("7. History")
            print("8. Exit")

            Operator = input("Enter choice: ")

            # HISTORY OPTION (no numbers needed)
            if Operator == "7":
                print("\n--- HISTORY ---")
                for i in History:
                    print(i)
                continue

            # EXIT
            if Operator == "8":
                print("Exiting calculator. Goodbye!")
                break

            # take numbers ONLY if needed
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            result = None

            if Operator == "1" or Operator == "+":
                result = num1 + num2
                op = "+"

            elif Operator == "2" or Operator == "-":
                result = num1 - num2
                op = "-"

            elif Operator == "3" or Operator == "*":
                result = num1 * num2
                op = "*"

            elif Operator == "4" or Operator == "/":
                result = num1 / num2
                op = "/"

            elif Operator == "5" or Operator == "%":
                result = num1 % num2
                op = "%"

            elif Operator == "6" or Operator == "^":
                result = num1 ** num2
                op = "^"

            else:
                print("Invalid operator")
                continue

            print(f"Result: {result}")

            # store safely
            History.append({
                "num1": num1,
                "num2": num2,
                "operator": op,
                "result": result
            })

        except ValueError:
            print(" Invalid input. Please enter numbers only.")

        except ZeroDivisionError:
            print(" Cannot divide by zero!")

        except Exception as error:
            print(" Error:", error)

calculator()