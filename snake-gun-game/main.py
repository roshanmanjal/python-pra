import random

"""
Snake Water Gun game
1 for Snake
-1 for water
0 gun
"""
# computer = -1    first we fixed it, then we can change by random..
computer = random.choice([1, 0, -1])  # witrh random module it chooses on its own
youstr = input(("s = Snake, w = Water, g = Gun\nEnter your choice:- "))
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if computer == you:
    print("its a DRAW..")       
else:
    if computer == -1 and you == 1:
        print("You win !!!")
    elif computer == -1 and you == 0:
        print("You Loose !!!")
    elif computer == 1 and you == 0:
        print("You win !!!")
    elif computer == 1 and you == -1:
        print("You Loose !!!")
    elif computer == 0 and you == -1:
        print("You win !!!")
    elif computer == 0 and you == 1:
        print("You Loose !!!")
    else:
        print("Something went wrong, Try again...")
    print("Thank you for playing this game..")
