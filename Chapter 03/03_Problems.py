name = input("Enter your name:- ")
print("Good Night", name)
# another way to write 
print(f"Good Morning {name}") # make if as f string to wirte name 

# problem 2 print name and date pgm

letter = '''
        Dear <|Name|>,
        You are selected for Data Analyst at Accenture and you can join from
        <|Date|>
        '''
print(letter.replace("<|Name|>", "Roshan").replace("<|Date|>", "06 December"))

# to find any word 
name = ("Today is Sunday")
print(name.find('Sun')) # at 9th index