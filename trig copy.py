import math

def calculator():
    print("Scientific Calculator")
    try:
        while True:
            op = input("Enter operation (sin, cos, tan, sqrt, log, ln, pow) or type exit: ").strip().lower()
            if op == "exit":
                print("Exiting the calculator")
                break

            list_op = ["sin", "cos", "tan", "sqrt", "log", "ln", "pow"]
            if op not in list_op:
                print("Please enter a valid operator")
                continue

            try:
                if op in ["sin", "cos", "tan", "sqrt", "log", "ln"]:
                    number = float(input("Enter number: "))
                    if op == "sin":
                        result = math.sin(math.radians(number))
                        print(f"sin({number}) = {result}")
                    elif op == "cos":
                        result = math.cos(math.radians(number))
                        print(f"cos({number}) = {result}")
                    elif op == "tan":
                        result = math.tan(math.radians(number))
                        print(f"tan({number}) = {result}")
                    elif op == "sqrt":
                        if number < 0:
                            print("Error: Cannot take square root of a negative number!")
                        else:
                            result = math.sqrt(number)
                            print(f"√{number} = {result}")
                    elif op == "log":
                        if number <= 0:
                            print("Error: log(x) only works for x > 0")
                        else:
                            result = math.log10(number)
                            print(f"log({number}) = {result}")
                    elif op == "ln":
                        if number <= 0:
                            print("Error: ln(x) only works for x > 0")
                        else:
                            result = math.log(number)
                            print(f"ln({number}) = {result}")

                elif op == "pow":
                    base = float(input("Enter base (x): "))
                    exp = float(input("Enter exponent (y): "))
                    result = math.pow(base, exp)
                    print(f"{base}^{exp} = {result}")

            except ValueError:
                print("Invalid input! Please enter a valid number.")

    except KeyboardInterrupt:
        print("\nCalculator interrupted. Goodbye!")

calculator()