# Start

# This is for choosing add, subtract, multiply or divide
print("This is an python calculator.")
equation = input("Enter add, subtract, multiply or divide to start you calculations: ")

# This is for addition
if equation == "add" :
    inp1 = input("Enter a value: ")
    inp2 = input("Enter another value: ")
    result = int(inp1) + int(inp2)
    print("Addition of", inp1, "and", inp2, "is", result)

# This is for subtraction
if equation == "subtract" :
    num1 = input("Enter a value: ")
    num2 = input("Enter another value: ")
    num1and2 = int(num1) - int(num2)
    print("Subtraction of", num1, "and", num2, "is", num1and2)

# This is for multiplication
if equation == "multiply" :
    input1 = input("Enter a value: ")
    input2 = input("Enter another value: ")
    answer = int(input1) * int(input2)
    print("Multiplication of", input1, "and", input2, "is", answer)

# This is for division
if equation == "divide" :
    number1 = input("Enter a value: ")
    number2 = input("Enter another value: ")
    quotient = int(number1) / int(number2)
    print("Division of", number1, "and", number2, "is", quotient)

# End