marks = (12,12,23,443,45,45,3,23)
print(marks) # it will not print the duplicate values
marks.add(100) # it will add 100 to the set
print(marks[0]) # it will give error because set is unordered and unindexed


# to print as index use for loop
print("For Loop started to print as index")
for score in marks:
    print(score)