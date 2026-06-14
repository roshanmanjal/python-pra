# pgm to print sum of n numbers


def sum(num):
    if num == 0:
        return 0
    return sum(num - 1) + num


num = int(input("Enter your number for sum :- "))
ans = sum(num)
print("Your sum is - ", ans)