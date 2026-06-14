from functools import reduce 
# Use reduce method to reduce number that are greater than 100 from a list of numbers.

def greater(a,b):
    if(a>b):
        return a
    return b

l = [1,3,4,36,45,57,44,555,66]
print(reduce(greater,l))