# to print stars by user
def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n-1)
    
b = int(input("Enter the number to print star :- "))
pattern(b)