class students:
    a = 36
    
    def show(students):
        print(f"The class attribute of student a is = {students.a}")  # cls can be written here at {student.a}

s = students()
s.a = 32
s.show() # this will print value 36 but if i want to print class value we will -

class students:
    a = 36
    @classmethod # add a decorater here this will print value as 36
    def show(students):
        print(f"The class attribute of student a is = {students.a}")

s = students()
s.a = 32
s.show()