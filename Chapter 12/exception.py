try:
    a = int(
        input("Enter a number: ")
    )  # try is used to take int but if it fails it goes to except
    print(a)
except (
    ValueError
):  # except block is used to catch the error and show user a valid message
    print("Please enter a valid integer.")

# 2nd method
while True:  # while loop is used to keep asking user until valid input is given
    try:
        a = int(input("Enter a number: "))  # try block to take input again
        break
    except ValueError:  # except block to catch error again
        print("Please enter a valid integer.")

# this is a raise except
# where we can raise and print custom error lines
if a == 0:
    raise ZeroDivisionError("You entered zero, which is not allowed.")

print("Thank you!")  # this will get printed as except show valid msg so no error user will retry