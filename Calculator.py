def welcome():
    print("Welcome to my Calculator Project")

def add(num1, num2):
        return num1 + num2

def subtract(num1, num2):
        return num1 - num2

def multiply(num1, num2):
        return num1 * num2

def divide(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
while True:
    welcome()

    print("Welcome to my Calculator Project")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator(+, -, *, /): ")
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid numbers.")
        continue

    if operator == "+":
        result = add(num1 , num2)
        print("Result: ", result)

    elif operator == "-":
        result = subtract(num1 , num2)
        print("Result: ", result)

    elif operator == "*":
        result = multiply(num1 , num2)
        print("Result: ", result)

    elif operator == "/":
        if num2 != 0:
                 result = divide(num1 , num2)
                 print("Result: ", result)
        else:
         print("Error: Cannot divide by zero")

    else:
         print("Invalid operator")

    again = input("Do you want to calculate again? (yes/no): ").lower()

    if again == "yes":
        continue
    else:
        print("Please enter yes or no.")

