# Function to add two numbers
def add(a, b):
    return a + b


# Function to subtract two numbers
def subtract(a, b):
    return a - b


# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Function to divide two numbers
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"


# Main calculator loop
while True:

    # Display calculator menu
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Get user's choice
    choice = input("Enter your choice (1-5): ")

    # Exit the program
    if choice == "5":
        print("Exiting calculator...")
        break

    # Check if the choice is valid
    if choice in ["1", "2", "3", "4"]:

        # Get two numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))

    else:
        print("Invalid choice. Please select from 1 to 5.")