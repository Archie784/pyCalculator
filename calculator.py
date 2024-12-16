import math
from datetime import datetime

# operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: You can't divide by zero."
    return x / y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(x)

# display the main menu
def display_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. More...")

# display the 'More' menu
def display_more_menu():
    print("\nMore options:")
    print("1. Square Root")
    print("2. History")

# main program
def main():
    history = []
    operations = {
        '1': (add, '+'),
        '2': (subtract, '-'),
        '3': (multiply, '*'),
        '4': (divide, '/')
    }
    
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice in operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                operation, symbol = operations[choice]
                result = operation(num1, num2)
                print(f"Result: {result}")
                history.append(f"{datetime.now()}: {num1} {symbol} {num2} = {result}")
            except ValueError:
                print("Invalid number input.")
        elif choice == '5':
            display_more_menu()
            more_choice = input("Enter choice (1/2): ")
            
            if more_choice == '1':
                try:
                    num = float(input("Enter number: "))
                    result = square_root(num)
                    print(f"√{num} = {result}")
                    history.append(f"{datetime.now()}: √{num} = {result}")
                except ValueError:
                    print("Invalid number input.")
            elif more_choice == '2':
                print("\nCalculation History:")
                if history:
                    print("\n".join(history))
                else:
                    print("No history available.")
            else:
                print("Invalid input in 'More' menu.")
        else:
            print("Invalid input.")

        next_calculation = input("\nDo another calculation? (yes/no): ").strip().lower()
        if next_calculation != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
