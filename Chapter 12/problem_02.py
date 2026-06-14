# print table of a number with a list comprehension
n = int(input("Enter a number to print its table: ")) # takes input form user
table = [n * i for i in range(1, 11)]  # for line and our multiply in 1 line only 
print(f"Table of {n}: {table}")  