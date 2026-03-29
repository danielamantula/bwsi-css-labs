"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""
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
    def simple_calculator(final_num1: float, final_num2: float) -> float:
        while True: 
            try:
                operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
                if operation == "add":
                    return final_num1 + final_num2, operation
                elif operation == "subtract":
                    return final_num1 - final_num2, operation
                elif operation == "multiply":
                    return final_num1 * final_num2, operation
                elif operation == "divide":
                    if final_num2 != 0:
                        return final_num1 / final_num2, operation
                    else:
                        raise ValueError("Cannot divide by zero.")
                else:
                    raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
            except ValueError as ve:
                print(ve)
                continue
    result, opinfo = simple_calculator(final_num1, final_num2)
    print(f"The result of {opinfo}ing {final_num1} and {final_num2} is: {result}.")
if __name__ == "__main__":
    main()
