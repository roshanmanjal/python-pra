# Using walrus operator to assign and check length of a list
if(n:= len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
    # o./p List is too long (5 elements, expected <= 3)