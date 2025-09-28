
def calculate():
    global num1, num2, operator

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

num1 = 0
num2 = 0
operator = ''

while True:
    print("\n--- New Calculation ---")
    try:
        
        num1_input = input("Enter the first number (or 'exit' to quit): ")
        if num1_input.lower() == 'exit':
            break
        num1 = float(num1_input)

        operator = input("Enter an operator (+, -, *, /): ")

        num2_input = input("Enter the second number: ")
        num2 = float(num2_input)

   
        result = calculate()
        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print("An unknown error occurred:", e)

print("Calculator closed.")
