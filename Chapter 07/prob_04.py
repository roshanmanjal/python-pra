# # print stars **
n = int(input("Enter the number:- "))
for i in range(1, n+1):
    print(" "* (n-i), end="") # add space in start of line
    print("*" * (i), end="")
    print(" ")
    
    
print("*" * (2*i-1), end="")  # prints different stars type see practice set


# also other type
# * * *
# *  *   see middle gap
# * * *   

n = int(input("Enter the number:- "))
for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n)
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
        print("") 