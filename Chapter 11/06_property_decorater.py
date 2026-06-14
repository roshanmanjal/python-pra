# encapsulation and abstraction used here
class students:
    a = 36

    def show(students):
        print(
            f"The class attribute of student a is = {students.a}"
        )  # cls can be written here at {student.a}

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]


s = students()
s.name = "Roshan Manjal"
print(s.fname, s.lname)
s.show()
