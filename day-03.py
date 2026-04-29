# day-03.py
# caluculator with functions

def add(a, b):
    return a + b

def substract(a, b):
    return a - b 

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "cannot devided by zero"
    return a / b

#Main Program
print("welcome to my calculator")
print("operators: +, -, *, /")

operation = input("enter operation: ")
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = substract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "invalid operation" 
print("result: ", result)
