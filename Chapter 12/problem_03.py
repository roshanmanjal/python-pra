    # to create a file of tables ising list comprehension
    # print table of a number with a list comprehension
    
n = int(input("Enter a number to print its table: "))                  # takes input form user
with open("tables.txt", "a") as f:                                # open file in append mode
    table = [n * i for i in range(1, 11)]                        # for line and our multiply in 1 line only 
    f.write(f"Table of {n}: {table}\n")                            # this will print table in list format 