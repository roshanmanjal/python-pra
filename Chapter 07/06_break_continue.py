# break
for i in range(100):
    if(i == 34):  # as 34 will break it will break as it is 
        break
    print(i)
    
# continue
for i in range(100):
    if(i == 34):  # as 34 will skip 34 and continues till end of range
        continue
    print(i)
    
for i in range(4):
    print("Roshan")
    if i == 2:
        continue
    print(i)
    
# pass statement is used in for loops it instructs to do nothing it just pass its code 
for i in range(544):
  pass
# like if for loop to do later we leave it and pass
i = 0
while(i<=36):
    print(i)