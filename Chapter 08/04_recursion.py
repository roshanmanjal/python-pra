# print factorial of a number
# factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)
n = int(input("Enter the number:- "))
print("The factorial of a number is:- ", factorial(n))  

# in for loop also 
n = int(input("Enter the number:- "))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print("The factorial of number is:- ", fact)