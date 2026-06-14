myList = [1,2,3,45,16]
squareList = [i*i for i in myList]   # this is list comprehensive less code 
print(squareList)      

# normal code 
myList = [1,2,3,4,5]
squareList = []
for items in myList:    # this is long code 
    squareList.append(items*items)
print(squareList)