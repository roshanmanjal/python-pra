from functools import reduce
# map example
l = [1, 2, 3, 4, 5]
square = lambda n: n*n
print(tuple(map(square, l)))

# filter example
def even(n):
    if(n%2 == 0):
        return True
    return False
print(list(filter(even, l)))  # list will give o.utput in list format
# filter will return only those elements for which the function returns True
#even and l are function and the list above

# Reduce example
def sum(a, b):
    return a+b
print(reduce(sum, l))  # reduce will apply the function cumulatively to the items of the list
# sum and l are function and the list above sum is called automatically and it does like merge of all elements adding them