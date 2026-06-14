first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    result = first + second
    print("The result is: ", result)
elif operator == "-":
    result = first - second
    print("The result is: ", result)    
elif operator == "*":
    result = first * second
    print("The result is: ", result)
elif operator == "/":
    result = first // second
    print("The result is:", result)
else:    print("Invalid operator")
print("Thank you for using the calculator!")