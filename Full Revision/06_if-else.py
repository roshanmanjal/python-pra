age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
    print("You can vote.")
elif age >= 13 and age < 18:
    print("You are a teenager.")
    print("You cannot vote.")
else:
    print("You are a minor.")
    print("You cannot vote.")   
    print("Thank You")
    