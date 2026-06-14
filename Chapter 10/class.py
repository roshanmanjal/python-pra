# take input form user with this code using self
# self is not inbuilt function
class Student:
    def __init__(self, name, marks):  # it runs on its own when object is called no need to call seperatly   __ underscore wle ase hote h
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


# taking input outside the class
name1 = input("Enter name of student 1: ")
marks1 = int(input("Enter marks of student 1: "))

name2 = input("Enter name of student 2: ")
marks2 = int(input("Enter marks of student 2: "))

# creating two different objects
s1 = Student(name1, marks1)
s2 = Student(name2, marks2)

# displaying data
print("\nStudent 1 Details")
s1.show()

print("\nStudent 2 Details")
s2.show()