# need to understand  this code
# Employee class
class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name  # stored in THIS object
        self.salary = salary  # stored in THIS object

    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}")


# Coder class
class Coder:
    language = "Python"

    def printLanguage(self):
        print(f"Your Language: {self.language}")


# Programmer inherits from Employee and Coder
class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showAll(self):
        print(f"[Programmer.showAll] self = {self}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")
        print(f"Language: {self.language}")


# ----- OBJECT CREATION -----
emp = Employee("Roshan", 120000)
prog = Programmer("Amit", 150000)
print("\n--- Employee Object ---")
emp.show()
print("\n-- Programmer Object --")
prog.show()
prog.printLanguage()
prog.showAll()
