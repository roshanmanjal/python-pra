from typing import List, Dict, Tuple
#we can use multiple vaariable in multi types
n : int = 3  # this we said that n is integer with value 3 with :int
m : float = 4.5  # this we said that m is float with value 4.5 with :float
s : str = "hello"  # this we said that s is string with value "hello" with :str

def sum(a :int , b :int) -> int:  # this we said that a and b are integers and the function returns an integer with ->int
    return a + b

s = sum(12,34)
print(s)
 # this is done for clear syntax and better code readability and to avoid errors