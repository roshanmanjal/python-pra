# problems on dict n sets
words = {
    "madad" : "Help",
    "Chai" :"Tea",
    "Kitab" : "Book",
}
word = input("Enter your word:- ")
print(words[word])

# 2nd problem  to take 8 numbers and print the set
s = set()
n = input("Enter your number:- ")
s.add(int(n))
n = input("Enter your number:- ")
s.add(int(n))
n = input("Enter your number:- ")
s.add(int(n))
n = input("Enter your number:- ")
s.add(int(n))
n = input("Enter your number:- ")
s.add(int(n))
n = input("Enter your number:- ")
s.add(int(n))
n = input("Enter your number:- ")
s.add(int(n))
n = input("Enter your number:- ")
s.add(int(n))

print(s) # we can see it only prints single not duplicates

# 3rd prob
s = set()
s.add(18) # it will add as an int
s.add("18")   # it will add as string
print(s) 