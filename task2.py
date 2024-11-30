#this is task2 (simple calculator) created by Rohan Tripathi 
print("Calculator")
print("Operations: +, -, *, /")
num1 = float(input("Enter the first number:"))
operator = input("Enter an operator (+, -, *, /):")
num2 = float(input("Enter the second number:"))
if operator == '+':
            result = num1 + num2
elif operator == '-':
            result = num1 - num2
elif operator == '*':
            result = num1 * num2
elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
else:
    print("Invalid operator!")
print(f"The result is: {result}")