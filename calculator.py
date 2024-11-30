import math  # needed for the square root thing

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: You can't divide by zero."
    else:
        return x / y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(x)

# to save history
history = []

# main things idk
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.More...")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        if choice == '5':
            # extras
            print("More options:")
            print("1.Square Root")
            print("2.History")
            more_choice = input("Enter choice(1/2): ")

            if more_choice == '1':
                num = float(input("Enter number: "))
                result = square_root(num)
                print("√", num, "=", result)
                history.append(f"√{num} = {result}")
            elif more_choice == '2':
                print("Calculation History:")
                if history:
                    for entry in history:
                        print(entry)
                else:
                    print("No history available.")
            else:
                print("Invalid Input in 'More' menu.")

        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print(num1, "+", num2, "=", result)
                history.append(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(num1, "-", num2, "=", result)
                history.append(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(num1, "*", num2, "=", result)
                history.append(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(num1, "/", num2, "=", result)
                history.append(f"{num1} / {num2} = {result}")

        # Ask if user wants to do another calculation
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            break
    else:
        print("Invalid Input")
