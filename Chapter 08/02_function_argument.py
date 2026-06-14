# if we want to add argument in functions
def GoodDay(name):  # name is an argument it will take when called 
    print("Happy Good Day To You " + name)  # concatenate with name
    return "Done"    # now it will print done at none place

# return term
a = GoodDay("Soham")
print(a)  # it will print none 
 
GoodDay("Roshan")
GoodDay("Rajesh")  # it will also print again with Rajesh