"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def main():
    
    print(f"===== Simple Calculator =====")
    # Ask the user for sample input    
    while True:
        try:
            num1 = input("Enter the first number: ")
            final_num1 = float(num1)
        except ValueError:
            print("\n That is not a valid first value! Please enter another value, with no letters or extraneous elements.")
            continue
        break
    while True:
        try:
            num2 = input("Enter the second number: ") 
            final_num2 = float(num2)
        except ValueError:
            print("\n That is not a valid second value! Please enter another value, with no letters or extraneous elements.")
            continue
        break
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    result = simple_calculator(operation, final_num1, final_num2)
    print(f"The result of {operation}ing {final_num1} and {final_num2} is: {result}")
if __name__ == "__main__":
    main()
