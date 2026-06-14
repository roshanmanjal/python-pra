# ise filter method to filter number that are divisible by 3 from a list of numbers.

def divisible(num):
    if(num%3 == 0):
        return True
    return False

num = [3,9,23,33,564,42,34,34,23,34,3423,56,67,27,36]
final = list(filter(divisible, num))
print(final)