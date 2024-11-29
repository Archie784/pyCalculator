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
# ask what type of calculation the user wants to do
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square Root")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        if choice == '5':
            num = float(input("Enter number: "))
            print("√", num, "=", square_root(num))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

        # ask if user wants to do another calculation
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            break
    else:
        print("Invalid Input")
