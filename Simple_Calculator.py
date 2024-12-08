def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("Simple Calculator")
    print("Enter 'q' to quit")
    while True:
        operation = input("Choose operation (add, subtract, multiply, divide): ")
        if operation == 'q':
            print("Goodbye!")
            break
        if operation in ('add', 'subtract', 'multiply', 'divide'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if operation == 'add':
                print(f"Result: {add(num1, num2)}")
            elif operation == 'subtract':
                print(f"Result: {subtract(num1, num2)}")
            elif operation == 'multiply':
                print(f"Result: {multiply(num1, num2)}")
            elif operation == 'divide':
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    calculator()
