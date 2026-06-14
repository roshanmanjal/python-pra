name = "Roshan Manjal"
print(name.upper())
print(name.lower())
print(name.title())
print(name[0])
print(name[0:6]) # [start:stop] stop is exclusive it stops one before the index

print(name.find("M"))  # find the index of the first occurrence of the specified value so this is at index 7

print(name.replace("Roshan", "Raja"))

print('R' in name) # it will give true.
print('r' in name)  # this is false because it is case sensitive