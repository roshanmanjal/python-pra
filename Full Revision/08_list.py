marks = [15,19,16, "SSD"]
print(marks)
print(type(marks)) #list is a data structure which can store multiple values of different data types
print(marks[0]) #list is a zero indexed data structure
print(marks[1])
print(marks[-1]) #negative indexing is used to access the last element of the list
print(marks[0:3])
marks.append((99)) #append is used to add an element at the end of the list
print(marks) #marks.remove("SSD") #remove is used to remove an element from the list
marks.insert(1,18) #insert is used to add an element at a specific index in the list
print(marks)
print("for loop in list") # for loop is used to iterate through the elements of the list
for marks in marks: #marks is a variable which is used to store the value of the current element in the list
    print(marks)
    
marks.clear() #clear is used to remove all the elements from the list
print(marks)