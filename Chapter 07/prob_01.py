# # print table of number entered by user
n = int(input("Enter your number:- "))
for i in range(1,11):
    print(f"{n} * {i} = {n * i}")
    

# same prob in while loop
i = 1
while(i <= 10):
    print(f"{n} * {i} = {n * i}")
    i = i + 1