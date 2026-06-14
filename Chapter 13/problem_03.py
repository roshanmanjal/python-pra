# to create table of 7 as list ansd then convert to string n print vertically

table = [str(7*i) for i in range(1, 11)]
s = "\n".join(table) # joion method to create a single string with new lines
print(s)