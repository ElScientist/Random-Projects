num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another Number: "))
operator = input("Enter a Operator: ")

def add():
    print(num1 + num2)

def subtract():
    print(num1 - num2)

def multiply():
    print(num1 * num2)

def divide():
    print(num1 / num2)

if operator == "+":
    add()
elif operator == "-":
    subtract()
elif operator == "*":
    multiply()
elif operator == "/":
    divide()
else:
    print("Invalid Operator")
