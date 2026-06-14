# read the file and checks for the word present or not
f = open("poem.txt")
n = input("Enter your word:- ")

word = f.read()
if(n in word):
    print("Thw word is present..")
else:
    print("The word is not present..")
f.close()
