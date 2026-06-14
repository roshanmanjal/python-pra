from random import randint
n = randint(1, 1000)
a = -1
guesses =  1
while(a != n):
    a = int(input("Guess a number:- "))
    if(a < n):
        print("Higher number please!")
        guesses = guesses + 1
    elif(a > n):
        print("Lower number please!")
        guesses = guesses + 1  
    else:
        print(f"You guessed {a} in {guesses} tries!")
        break
print("Thank you for playing!")